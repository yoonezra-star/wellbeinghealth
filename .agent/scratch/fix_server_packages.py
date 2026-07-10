import paramiko
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

hostname = "129.212.235.171"
username = "master_zmuwemtfup"
password = "VjdUUR4pRsTj"

def run(ssh, cmd, timeout=60):
    stdin, stdout, stderr = ssh.exec_command(cmd, timeout=timeout)
    out = stdout.read().decode("utf-8", errors="replace").strip()
    err = stderr.read().decode("utf-8", errors="replace").strip()
    return out, err

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname, username=username, password=password)
print("SSH Connected OK")

print("\n=== Installing schedule, python-dotenv... ===")
out, err = run(ssh, "pip3 install schedule python-dotenv --quiet 2>&1", timeout=120)
print(out if out else "(출력 없음)")
if err: print("ERR:", err)

print("\n=== Verifying installation ===")
out, err = run(ssh, "pip3 show schedule python-dotenv 2>&1 | grep -E 'Name|Version'")
print(out)

print("\n=== Import test ===")
out, err = run(ssh, "cd ~/wellbeing_auto && python3 -c 'import schedule, dotenv; print(\"import OK\")'")
print("OUT:", out)
if err: print("ERR:", err)

print("\n=== Current Crontab ===")
out, err = run(ssh, "crontab -l")
print(out)

print("\n=== Server Timezone ===")
out, _ = run(ssh, "date && cat /etc/timezone")
print(out)

print("""
=== 진단 결과 ===
- 서버 시간대: UTC
- 한국시간(KST) = UTC + 9시간
- 오전 10시 KST = 01:00 UTC  (현재 크론: 0 1 * * *)  ✅ 맞음
- 오후 3시 KST  = 06:00 UTC  (현재 크론: 0 6 * * *)  ✅ 맞음
""")

ssh.close()
print("Done.")
