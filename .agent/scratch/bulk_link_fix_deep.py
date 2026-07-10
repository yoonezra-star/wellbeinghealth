import paramiko
import sys
import io
import os
import base64
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

hostname = "129.212.235.171"
username = "master_zmuwemtfup"
password = "VjdUUR4pRsTj"

SERVER_SCRIPT = '''import os
import requests
import re
from requests.auth import HTTPBasicAuth
from dotenv import load_dotenv

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
load_dotenv(os.path.join(SCRIPT_DIR, ".env"))

WP_URL = os.getenv("WP_URL")
auth = HTTPBasicAuth(os.getenv("WP_USERNAME"), os.getenv("WP_APP_PASSWORD"))

def fix_links_in_content(content):
    # 더 유연한 정규표현식: [제목] (주소) 또는 [제목](주소) 모두 대응
    # [(글제목)]( (http...) )
    pattern = r'\\[(.*?)\\]\\s*\\((https?://[^\\s)]+)\\)'
    new_content = re.sub(pattern, r'<a href="\\2">\\1</a>', content)
    return new_content

def process_all_posts():
    print("Starting deep scan of all posts for raw markdown links...")
    page = 1
    total_fixed = 0
    total_scanned = 0
    
    while True:
        # context=edit 를 사용하여 원본 raw 데이터를 가져옴
        r = requests.get(f"{WP_URL}/wp-json/wp/v2/posts?per_page=100&page={page}&context=edit", auth=auth, timeout=30)
        if r.status_code != 200:
            break
            
        posts = r.json()
        if not posts:
            break
            
        for post in posts:
            total_scanned += 1
            post_id = post["id"]
            # 원본 raw 콘텐츠 사용
            raw_content = post["content"]["raw"]
            
            # 마크다운 링크 패턴 검색
            if re.search(r'\\[.*?\\]\\s*\\(https?://', raw_content):
                fixed_content = fix_links_in_content(raw_content)
                
                # 내용이 변경되었을 때만 업데이트
                if fixed_content != raw_content:
                    update_data = {"content": fixed_content}
                    up_r = requests.post(f"{WP_URL}/wp-json/wp/v2/posts/{post_id}", auth=auth, json=update_data, timeout=30)
                    
                    if up_r.status_code == 200:
                        print(f"Post {post_id}: Links converted to HTML.")
                        total_fixed += 1
                    else:
                        print(f"Post {post_id}: Update failed ({up_r.status_code})")
        
        page += 1
        
    print(f"\\nScan complete. Total posts scanned: {total_scanned}, Total posts fixed: {total_fixed}")

if __name__ == "__main__":
    process_all_posts()
'''

def run(ssh, cmd, timeout=900):
    stdin, stdout, stderr = ssh.exec_command(cmd, timeout=timeout)
    out = stdout.read().decode("utf-8", errors="replace").strip()
    err = stderr.read().decode("utf-8", errors="replace").strip()
    return out, err

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname, username=username, password=password)
print("SSH Connected OK")

encoded = base64.b64encode(SERVER_SCRIPT.encode("utf-8")).decode("ascii")
run(ssh, "rm -f ~/wellbeing_auto/deep_fix_links.b64")

chunk_size = 1000
chunks = [encoded[i:i+chunk_size] for i in range(0, len(encoded), chunk_size)]
for chunk in chunks:
    run(ssh, f"echo -n '{chunk}' >> ~/wellbeing_auto/deep_fix_links.b64")

run(ssh, "base64 -d ~/wellbeing_auto/deep_fix_links.b64 > ~/wellbeing_auto/deep_fix_links.py")
print("Upload Complete.")

print("\\n=== Running Deep Link Fix Script ===")
out, err = run(ssh, "cd ~/wellbeing_auto && /usr/bin/python3 deep_fix_links.py", timeout=900)
print(out)
if err: print("ERR:", err)

ssh.close()
