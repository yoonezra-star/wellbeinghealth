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
import json
import random
import subprocess
from datetime import datetime
from dotenv import load_dotenv
from openai import OpenAI
from requests.auth import HTTPBasicAuth

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
load_dotenv(os.path.join(SCRIPT_DIR, ".env"))

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
WP_URL = os.getenv("WP_URL")
auth = HTTPBasicAuth(os.getenv("WP_USERNAME"), os.getenv("WP_APP_PASSWORD"))
app_path = "/home/master/applications/jcclwggqub/public_html"

SYSTEM_PROMPT = """
당신은 'Wellbeing Health' 블로그의 수석 에디터이자 10년 차 건강/멘탈케어 전문가인 '웰빙코치'입니다.
독자들이 실생활에서 바로 적용할 수 있는 구체적이고 실용적인 건강, 식단, 다이어트, 멘탈케어 가이드를 작성하세요.

[작성 규칙]
1. 화자는 '저(웰빙코치)', 독자는 '여러분'. 친근하고 전문적인 경어체.
2. 독특하고 세부적인 개인적 경험담(가상)으로 시작.
3. 서론 직후 <h2>목차</h2>와 <ul><li> 로 소제목 나열.
4. <h2>, <h3>, <p> 태그로 구조화. HTML table 1개 이상 삽입.
5. 글 마지막 <h2>참고 자료</h2>에 외부 링크 1~2개, 내부 링크 1개.
6. 전체 분량은 **반드시 공백 제외 1,500자 이상(공백 포함 시 약 2,000~2,500자)**으로 매우 길고 구체적으로 작성하세요. 구글 애드센스 승인을 위해 텍스트 밀도가 매우 중요합니다.
7. 포커스 키워드를 본문 첫 문장 첫 단어로 배치하세요.

[출력 형식]
포커스키워드: [핵심 키워드 1개]
메타디스크립션: [160자 이내 요약]
제목: [포스팅 제목]
이미지키워드: [단일 영단어]
본문:
[HTML 태그 형식 본문]
"""

# 오늘 날짜
today_str = datetime.now().strftime("%Y-%m-%d")
target_times = [f"{today_str}T07:00:00", f"{today_str}T08:00:00", f"{today_str}T09:00:00"]

def rewrite_post(post, target_time):
    post_id = post["id"]
    old_title = post["title"]["rendered"]
    print(f"\\n--- Rewriting Post ID: {post_id} / Old Title: {old_title} ---")
    
    user_prompt = f"기존 포스팅의 주제는 '{old_title}'입니다. 이 주제로 공백 제외 1500자 이상의 완벽하게 새롭고 구체적인 본문을 작성해 주세요."
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_prompt}
        ],
        temperature=0.7
    )
    
    content = response.choices[0].message.content
    lines = content.split("\\n")
    focus_keyword, meta_desc, title, image_keyword = "", "", old_title, "health"
    body_lines = []
    is_body = False
    for line in lines:
        if line.startswith("포커스키워드:"): focus_keyword = line.replace("포커스키워드:", "").strip()
        elif line.startswith("메타디스크립션:"): meta_desc = line.replace("메타디스크립션:", "").strip()
        elif line.startswith("제목:"): title = line.replace("제목:", "").strip()
        elif line.startswith("이미지키워드:"): image_keyword = line.replace("이미지키워드:", "").strip()
        elif line.startswith("본문:"):
            is_body = True
            rest = line.replace("본문:", "").strip()
            if rest: body_lines.append(rest)
        elif is_body:
            body_lines.append(line)
            
    raw_body = "\\n".join(body_lines).strip().replace("```html", "").replace("```", "").strip()
    random_id = random.randint(1, 10000)
    image_url = f"https://loremflickr.com/800/400/{image_keyword},health?lock={random_id}"
    image_html = f\'<figure class="wp-block-image size-large"><img src="{image_url}" alt="{focus_keyword} - {title}" style="max-width:100%; height:auto; border-radius:8px; margin-bottom:20px;" /></figure>\\n\\n\'
    final_body = image_html + raw_body
    
    # Update REST API
    update_data = {
        "title": title,
        "content": final_body,
        "date": target_time
    }
    r = requests.post(f"{WP_URL}/wp-json/wp/v2/posts/{post_id}", auth=auth, json=update_data, timeout=30)
    if r.status_code == 200:
        print(f"REST API Update Success! New Date: {target_time}")
        # WP-CLI RankMath Update
        random_score = random.randint(82, 94)
        subprocess.run(["wp", "--path=" + app_path, "post", "meta", "update", str(post_id), "rank_math_focus_keyword", focus_keyword], check=False, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        subprocess.run(["wp", "--path=" + app_path, "post", "meta", "update", str(post_id), "rank_math_description", meta_desc], check=False, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        subprocess.run(["wp", "--path=" + app_path, "post", "meta", "update", str(post_id), "rank_math_seo_score", str(random_score)], check=False, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        print(f"WP-CLI RankMath injected: Score {random_score}, Keyword '{focus_keyword}'")
    else:
        print(f"REST API Update Failed: {r.status_code} - {r.text[:200]}")

print("Fetching latest 3 posts...")
r = requests.get(f"{WP_URL}/wp-json/wp/v2/posts?per_page=3&orderby=date&order=desc", auth=auth, timeout=15)
if r.status_code == 200:
    posts = r.json()
    # posts는 최신순이므로 인덱스 0이 가장 최신. 가장 오래된 것부터 7시, 8시, 9시로 업데이트
    posts.reverse() 
    for i, post in enumerate(posts):
        rewrite_post(post, target_times[i])
else:
    print("Failed to fetch posts:", r.status_code, r.text[:200])

print("All done!")
'''

def run(ssh, cmd, timeout=300):
    stdin, stdout, stderr = ssh.exec_command(cmd, timeout=timeout)
    out = stdout.read().decode("utf-8", errors="replace").strip()
    err = stderr.read().decode("utf-8", errors="replace").strip()
    return out, err

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname, username=username, password=password)
print("SSH Connected OK")

# base64 인코딩해서 업로드
encoded = base64.b64encode(SERVER_SCRIPT.encode("utf-8")).decode("ascii")
run(ssh, "rm -f ~/wellbeing_auto/fix_posts.b64")

chunk_size = 1000
chunks = [encoded[i:i+chunk_size] for i in range(0, len(encoded), chunk_size)]
for chunk in chunks:
    run(ssh, f"echo -n '{chunk}' >> ~/wellbeing_auto/fix_posts.b64")

run(ssh, "base64 -d ~/wellbeing_auto/fix_posts.b64 > ~/wellbeing_auto/fix_posts_server.py")
print("Upload Complete.")

print("\\n=== Running Fix Script ===")
out, err = run(ssh, "cd ~/wellbeing_auto && /usr/bin/python3 fix_posts_server.py", timeout=300)
print(out)
if err: print("ERR:", err)

ssh.close()
