import paramiko
import sys
import io
import os
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

hostname = "129.212.235.171"
username = "master_zmuwemtfup"
password = "VjdUUR4pRsTj"

LOCAL_CLEAN = r"c:\Users\yoone\Desktop\안티그래버티\wellbeinghealth\server_poster_clean.py"
REMOTE_PATH = "/home/master/wellbeing_auto/server_poster.py"

def run(ssh, cmd, timeout=30):
    stdin, stdout, stderr = ssh.exec_command(cmd, timeout=timeout)
    out = stdout.read().decode("utf-8", errors="replace").strip()
    err = stderr.read().decode("utf-8", errors="replace").strip()
    return out, err

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname, username=username, password=password)
print("SSH Connected OK")

# sftp.put 으로 파일 업로드
print("\n=== Uploading clean server_poster.py via sftp.put ===")
sftp = ssh.open_sftp()
sftp.put(LOCAL_CLEAN, REMOTE_PATH)
sftp.close()
print("Upload done!")

# 문법 체크
print("\n=== SYNTAX CHECK ===")
out, err = run(ssh, f"/usr/bin/python3 -m py_compile {REMOTE_PATH} && echo 'SYNTAX: OK'")
print(out)
if err and 'Error' in err: print("ERR:", err)

# 실행 테스트 (인자 없이 - 사용법 출력되면 OK)
print("\n=== QUICK RUN TEST (no args = should print usage) ===")
out, err = run(ssh, f"cd ~/wellbeing_auto && /usr/bin/python3 server_poster.py 2>&1")
print("OUT:", out)
if err: print("ERR:", err)

# 파일 앞부분 확인
print("\n=== First 12 lines (import check) ===")
out, _ = run(ssh, "head -12 ~/wellbeing_auto/server_poster.py")
print(out)

# 크론탭 최종 확인
print("\n=== CRONTAB (wellbeing lines only) ===")
out, _ = run(ssh, "crontab -l | grep wellbeing")
print(out if out else "(none)")

# 서버 시간 확인
print("\n=== Server time (UTC vs KST) ===")
out, _ = run(ssh, "date -u && TZ='Asia/Seoul' date")
print(out)

print("""
=== 크론 실행 스케줄 ===
  오전: UTC 01:00 = KST 10:00  -> 0 1 * * * morning
  오후: UTC 06:00 = KST 15:00  -> 0 6 * * * afternoon
""")

ssh.close()
print("=== DONE ===")
