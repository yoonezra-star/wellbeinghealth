import paramiko
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

hostname = "129.212.235.171"
username = "master_zmuwemtfup"
password = "VjdUUR4pRsTj"

def run(ssh, cmd, timeout=120):
    stdin, stdout, stderr = ssh.exec_command(cmd, timeout=timeout)
    out = stdout.read().decode("utf-8", errors="replace").strip()
    err = stderr.read().decode("utf-8", errors="replace").strip()
    return out, err

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname, username=username, password=password)
print("SSH Connected OK")

# 방법 1: --break-system-packages (빠른 방법)
print("\n=== Trying pip3 install with --break-system-packages ===")
out, err = run(ssh, "pip3 install schedule python-dotenv --break-system-packages --quiet 2>&1", timeout=120)
print(out if out else "(no output)")
if err: print("ERR:", err)

print("\n=== Verifying packages ===")
out, err = run(ssh, "pip3 show schedule python-dotenv 2>&1 | grep -E 'Name|Version'")
print(out if out else "(none)")

print("\n=== Import test ===")
out, err = run(ssh, "cd ~/wellbeing_auto && python3 -c 'import schedule; import dotenv; print(\"ALL PACKAGES OK\")'")
print("OUT:", out)
if err: print("ERR:", err)

# 크론탭에서 python3 경로를 /usr/bin/python3 으로 통일
print("\n=== Fixing crontab to use /usr/bin/python3 ===")
out, _ = run(ssh, "crontab -l")
print("Current crontab:")
print(out)

# wellbeing 크론잡 라인만 수정
new_cron_lines = []
for line in out.split('\n'):
    if 'wellbeing_auto' in line:
        # python3 -> /usr/bin/python3으로 교체
        line = line.replace('python3 /home/master/wellbeing_auto', '/usr/bin/python3 /home/master/wellbeing_auto')
    new_cron_lines.append(line)

new_cron = '\n'.join(new_cron_lines)
print("\nNew crontab:")
print(new_cron)

# crontab 업데이트
update_cmd = f"echo '{new_cron}' | crontab -"
out2, err2 = run(ssh, update_cmd)
if err2: print("Crontab update ERR:", err2)
else: print("Crontab updated OK!")

print("\n=== Final crontab ===")
out, _ = run(ssh, "crontab -l")
print(out)

# 즉시 테스트 실행 (오전 포스팅)
print("\n=== Running morning job IMMEDIATELY for testing ===")
print("(This will attempt to post to wellbeinghealth.co.kr)")
out, err = run(ssh, "cd ~/wellbeing_auto && /usr/bin/python3 server_poster.py morning >> cron.log 2>&1 &")
print("OUT:", out)
if err: print("ERR:", err)

import time
print("Waiting 10 seconds...")
time.sleep(10)

print("\n=== Checking cron.log after test ===")
out, err = run(ssh, "cat ~/wellbeing_auto/cron.log")
print(out if out else "(empty)")

ssh.close()
print("\nDone!")
