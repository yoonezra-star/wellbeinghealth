import paramiko
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

hostname = "129.212.235.171"
username = "master_zmuwemtfup"
password = "VjdUUR4pRsTj"

def run(ssh, cmd, timeout=180):
    stdin, stdout, stderr = ssh.exec_command(cmd, timeout=timeout)
    out = stdout.read().decode("utf-8", errors="replace").strip()
    err = stderr.read().decode("utf-8", errors="replace").strip()
    return out, err

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname, username=username, password=password)
print("SSH Connected OK")

print("\n" + "="*60)
print("[STEP 1] SYNTAX CHECK")
print("="*60)
out, err = run(ssh, "cd ~/wellbeing_auto && /usr/bin/python3 -m py_compile server_poster.py && echo 'SYNTAX: OK'")
print(out)
if err and 'Error' in err: print("ERR:", err)

print("\n" + "="*60)
print("[STEP 2] ACTUAL END-TO-END RUN (afternoon post)")
print("This will post to wellbeinghealth.co.kr")
print("="*60)
out, err = run(ssh, "cd ~/wellbeing_auto && /usr/bin/python3 server_poster.py afternoon 2>&1", timeout=180)
print(out if out else "(no output)")
if err: print("ERR:", err)

print("\n" + "="*60)
print("[STEP 3] CRON LOG after run")
print("="*60)
out, _ = run(ssh, "cat ~/wellbeing_auto/cron.log")
print(out if out else "(empty)")

print("\n" + "="*60)
print("[STEP 4] LATEST POSTS on WordPress (via API)")
print("="*60)
check_posts = """
import requests, os, sys
from requests.auth import HTTPBasicAuth
from dotenv import load_dotenv
load_dotenv()
wp = os.getenv('WP_URL')
auth = HTTPBasicAuth(os.getenv('WP_USERNAME'), os.getenv('WP_APP_PASSWORD'))
r = requests.get(wp+'/wp-json/wp/v2/posts?per_page=5&orderby=date&order=desc', auth=auth, timeout=15)
if r.status_code == 200:
    for p in r.json():
        print(f"  ID:{p['id']} | {p['date']} | {p['title']['rendered'][:40]}")
else:
    print("API ERROR:", r.status_code, r.text[:200])
"""
# 직접 SSH로 파이썬 실행
import base64
encoded = base64.b64encode(check_posts.encode()).decode()
out, err = run(ssh, f"cd ~/wellbeing_auto && echo '{encoded}' | base64 -d | /usr/bin/python3")
print(out if out else "(no output)")
if err: print("ERR:", err)

ssh.close()
print("\n" + "="*60)
print("FINAL VERIFICATION COMPLETE")
print("="*60)
