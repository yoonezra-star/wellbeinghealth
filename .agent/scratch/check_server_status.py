import paramiko

hostname = "129.212.235.171"
username = "master_zmuwemtfup"
password = "VjdUUR4pRsTj"

def run(ssh, cmd):
    stdin, stdout, stderr = ssh.exec_command(cmd)
    out = stdout.read().decode("utf-8", errors="replace").strip()
    err = stderr.read().decode("utf-8", errors="replace").strip()
    return out, err

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname, username=username, password=password)
print("SSH Connected OK")

print("\n=== 1. 서버 현재 시각 ===")
out, _ = run(ssh, "date && echo 'TZ:' && cat /etc/timezone 2>/dev/null")
print(out)

print("\n=== 2. 크론탭 설정 ===")
out, err = run(ssh, "crontab -l")
print(out if out else "(크론탭 없음)")
if err: print("ERR:", err)

print("\n=== 3. 크론 로그 (cron.log) ===")
out, err = run(ssh, "cat ~/wellbeing_auto/cron.log")
print(out if out else "(빈 로그)")
if err: print("ERR:", err)

print("\n=== 4. wellbeing_auto 디렉토리 파일 목록 ===")
out, err = run(ssh, "ls -lah ~/wellbeing_auto/")
print(out)

print("\n=== 5. Python3 경로 확인 ===")
out, err = run(ssh, "which python3 && python3 --version")
print(out, err)

print("\n=== 6. openai 패키지 설치 여부 ===")
out, err = run(ssh, "pip3 show openai 2>&1 | head -5")
print(out if out else "(없음)")
if err: print("ERR:", err)

print("\n=== 7. schedule 패키지 설치 여부 ===")
out, err = run(ssh, "pip3 show schedule 2>&1 | head -3")
print(out if out else "(없음)")
if err: print("ERR:", err)

print("\n=== 8. dotenv 패키지 설치 여부 ===")
out, err = run(ssh, "pip3 show python-dotenv 2>&1 | head -3")
print(out if out else "(없음)")
if err: print("ERR:", err)

print("\n=== 9. .env 파일 내용 확인 ===")
out, err = run(ssh, "cat ~/wellbeing_auto/.env")
print(out if out else "(없음)")
if err: print("ERR:", err)

print("\n=== 10. 봇 프로세스 실행 여부 ===")
out, err = run(ssh, "ps aux | grep server_poster | grep -v grep")
print(out if out else "(실행 중인 봇 없음)")

print("\n=== 11. 시스템 크론 로그 (최근 10줄) ===")
out, err = run(ssh, "grep CRON /var/log/syslog 2>/dev/null | tail -10 || journalctl -u cron 2>/dev/null | tail -10")
print(out if out else "(시스템 로그 확인 불가)")

ssh.close()
print("\nDone.")
