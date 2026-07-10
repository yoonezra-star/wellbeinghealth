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

print("\n" + "="*60)
print("1. schedule 패키지 실제 임포트 테스트")
print("="*60)
out, err = run(ssh, "/usr/bin/python3 -c 'import schedule; print(\"schedule OK:\", schedule.__version__)'")
print("OUT:", out)
if err: print("ERR:", err)

print("\n" + "="*60)
print("2. python-dotenv 실제 임포트 테스트")
print("="*60)
out, err = run(ssh, "/usr/bin/python3 -c 'from dotenv import load_dotenv; print(\"dotenv OK\")'")
print("OUT:", out)
if err: print("ERR:", err)

print("\n" + "="*60)
print("3. server_poster.py 전체 임포트 테스트 (핵심!)")
print("="*60)
out, err = run(ssh, "cd ~/wellbeing_auto && /usr/bin/python3 -c 'import sys; sys.argv=[\"\"]; exec(open(\"server_poster.py\").read().split(\"if __name__\")[0])' 2>&1")
print("OUT:", out if out else "(no output)")
if err and "Error" in err: print("ERR:", err)

print("\n" + "="*60)
print("4. 크론탭 설정 확인")
print("="*60)
out, _ = run(ssh, "crontab -l")
for line in out.split('\n'):
    if 'wellbeing' in line:
        print(">>> WELLBEING:", line)
    else:
        print("   ", line)

print("\n" + "="*60)
print("5. 크론 로그 전체 내용")
print("="*60)
out, err = run(ssh, "cat ~/wellbeing_auto/cron.log")
print(out if out else "(비어있음)")

print("\n" + "="*60)
print("6. 서버 시간 vs KST 비교")
print("="*60)
out, _ = run(ssh, "date -u && TZ='Asia/Seoul' date")
print(out)

print("\n" + "="*60)
print("7. 환경변수(.env) 로딩 테스트")
print("="*60)
out, err = run(ssh, "cd ~/wellbeing_auto && /usr/bin/python3 -c \"from dotenv import load_dotenv; import os; load_dotenv(); print('WP_URL:', os.getenv('WP_URL')); print('WP_USER:', os.getenv('WP_USERNAME')); print('OPENAI_KEY set:', bool(os.getenv('OPENAI_API_KEY')))\"")
print("OUT:", out if out else "(no output)")
if err: print("ERR:", err)

print("\n" + "="*60)
print("8. WordPress API 연결 테스트 (실제 인증 확인)")
print("="*60)
wp_test = """
import requests
from requests.auth import HTTPBasicAuth
from dotenv import load_dotenv
import os
load_dotenv()
url = os.getenv('WP_URL') + '/wp-json/wp/v2/posts?per_page=3&orderby=date&order=desc'
auth = HTTPBasicAuth(os.getenv('WP_USERNAME'), os.getenv('WP_APP_PASSWORD'))
r = requests.get(url, auth=auth, timeout=10)
print('Status:', r.status_code)
if r.status_code == 200:
    posts = r.json()
    for p in posts:
        print('  POST:', p['id'], p['date'], p['title']['rendered'][:30])
else:
    print('Error:', r.text[:200])
"""
# 파일로 저장 후 실행
sftp = ssh.open_sftp()
with sftp.open('/home/master/wellbeing_auto/wp_test.py', 'w') as f:
    f.write(wp_test)
sftp.close()

out, err = run(ssh, "cd ~/wellbeing_auto && /usr/bin/python3 wp_test.py", timeout=30)
print("OUT:", out if out else "(no output)")
if err: print("ERR:", err)

# 테스트 파일 삭제
run(ssh, "rm ~/wellbeing_auto/wp_test.py")

print("\n" + "="*60)
print("9. 다음 크론 실행 예정 시각")
print("="*60)
out, _ = run(ssh, "date -u && echo '--- Next cron runs (UTC) ---' && crontab -l | grep wellbeing")
print(out)

ssh.close()
print("\n" + "="*60)
print("진단 완료")
print("="*60)
