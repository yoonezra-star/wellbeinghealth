import paramiko
import sys
import io
import os
import base64
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

hostname = "129.212.235.171"
username = "master_zmuwemtfup"
password = "VjdUUR4pRsTj"

LOCAL_CLEAN = r"c:\Users\yoone\Desktop\안티그래버티\wellbeinghealth\server_poster_clean.py"
REMOTE_PATH = "/home/master/wellbeing_auto/server_poster.py"

def run(ssh, cmd, timeout=60):
    stdin, stdout, stderr = ssh.exec_command(cmd, timeout=timeout)
    out = stdout.read().decode("utf-8", errors="replace").strip()
    err = stderr.read().decode("utf-8", errors="replace").strip()
    return out, err

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname, username=username, password=password)
print("SSH Connected OK")

# 현재 파일 권한 확인
print("\n=== Current file permissions ===")
out, _ = run(ssh, "ls -la ~/wellbeing_auto/server_poster.py")
print(out)

# 권한 수정
print("\n=== Making file writable ===")
out, err = run(ssh, "chmod 664 ~/wellbeing_auto/server_poster.py")
print("chmod OK" if not err else f"ERR: {err}")

# base64로 파일 인코딩 후 전송
print("\n=== Encoding and uploading file via base64 ===")
with open(LOCAL_CLEAN, "rb") as f:
    file_content = f.read()
    
encoded = base64.b64encode(file_content).decode("ascii")

# 청크로 나눠서 전송 (너무 크면 한번에 안됨)
CHUNK_SIZE = 1000
chunks = [encoded[i:i+CHUNK_SIZE] for i in range(0, len(encoded), CHUNK_SIZE)]
print(f"Total chunks: {len(chunks)}")

# 임시 파일에 base64 데이터 쓰기
run(ssh, "rm -f ~/wellbeing_auto/tmp_upload.b64")
for i, chunk in enumerate(chunks):
    run(ssh, f"echo -n '{chunk}' >> ~/wellbeing_auto/tmp_upload.b64")
    if i % 10 == 0:
        print(f"  Progress: {i+1}/{len(chunks)} chunks")

print("Upload complete, decoding...")
out, err = run(ssh, "base64 -d ~/wellbeing_auto/tmp_upload.b64 > ~/wellbeing_auto/server_poster.py && rm ~/wellbeing_auto/tmp_upload.b64")
if err: print("ERR:", err)
else: print("Decode OK!")

# 문법 체크
print("\n=== SYNTAX CHECK ===")
out, err = run(ssh, f"/usr/bin/python3 -m py_compile {REMOTE_PATH} && echo 'SYNTAX: OK'")
print(out)
if err and 'Error' in err: print("ERR:", err)

# 실행 테스트
print("\n=== RUN TEST (no args) ===")
out, err = run(ssh, f"cd ~/wellbeing_auto && /usr/bin/python3 server_poster.py 2>&1")
print("OUT:", out)
if err: print("ERR:", err)

# 앞부분 확인
print("\n=== First 10 lines ===")
out, _ = run(ssh, "head -10 ~/wellbeing_auto/server_poster.py")
print(out)

ssh.close()
print("\n=== DONE ===")
