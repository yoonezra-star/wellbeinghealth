import paramiko
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

hostname = "129.212.235.171"
username = "master_zmuwemtfup"
password = "VjdUUR4pRsTj"

def run(ssh, cmd, timeout=30):
    stdin, stdout, stderr = ssh.exec_command(cmd, timeout=timeout)
    out = stdout.read().decode("utf-8", errors="replace").strip()
    err = stderr.read().decode("utf-8", errors="replace").strip()
    return out, err

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname, username=username, password=password)
print("SSH Connected OK")

# 서버에서 현재 server_poster.py 읽기
print("\n=== Reading current server_poster.py from server ===")
out, err = run(ssh, "head -15 ~/wellbeing_auto/server_poster.py")
print(out)

# 수정: schedule, paramiko, base64, time 제거 (크론이 스케줄 담당하므로 불필요)
# sed로 불필요한 import 제거
print("\n=== Removing unnecessary imports (schedule, paramiko, base64, time) ===")
cmds = [
    "sed -i '/^import schedule/d' ~/wellbeing_auto/server_poster.py",
    "sed -i '/^import paramiko/d' ~/wellbeing_auto/server_poster.py",
    "sed -i '/^import base64/d' ~/wellbeing_auto/server_poster.py",
    "sed -i '/^import time/d' ~/wellbeing_auto/server_poster.py",
]
for cmd in cmds:
    out, err = run(ssh, cmd)
    if err: print("ERR:", err)

# 확인
print("\n=== First 15 lines after fix ===")
out, _ = run(ssh, "head -15 ~/wellbeing_auto/server_poster.py")
print(out)

# 임포트 테스트
print("\n=== Import test (should pass now) ===")
out, err = run(ssh, "cd ~/wellbeing_auto && /usr/bin/python3 -c 'import sys; sys.path.insert(0,\".\"); from dotenv import load_dotenv; import requests, json, random, os; from datetime import datetime; from openai import OpenAI; from requests.auth import HTTPBasicAuth; print(\"ALL IMPORTS OK\")'")
print("OUT:", out)
if err: print("ERR:", err)

# 실제 server_poster.py 임포트 테스트
print("\n=== Full server_poster.py syntax check ===")
out, err = run(ssh, "cd ~/wellbeing_auto && /usr/bin/python3 -m py_compile server_poster.py && echo 'SYNTAX OK'")
print("OUT:", out)
if err: print("ERR:", err)

# 직접 실행 테스트 (인자 없이 실행해서 사용법 출력되면 OK)
print("\n=== Quick run test (no args) ===")
out, err = run(ssh, "cd ~/wellbeing_auto && /usr/bin/python3 server_poster.py 2>&1")
print("OUT:", out)
if err: print("ERR:", err)

print("\n=== Crontab (final) ===")
out, _ = run(ssh, "crontab -l")
for line in out.split('\n'):
    if 'wellbeing' in line:
        print(">>> ", line)
    else:
        print("    ", line)

ssh.close()
print("\n=== Done ===")
