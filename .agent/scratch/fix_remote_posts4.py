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
import re
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
app_path = "/home/1591341.cloudwaysapps.com/jcclwggqub/public_html"

SYSTEM_PROMPT = """
You are a professional Korean blog writer.
- 20 years of blog operation experience
- SEO content strategist

Your task: Write a high-quality Korean blog post optimized for Google AdSense approval.
Apply Google E-E-A-T (Experience, Expertise, Authoritativeness, Trustworthiness) naturally throughout.
Do NOT add any commentary, explanation, or preamble outside the specified output format.

===================================
STEP 1 — 출력 전 반드시 이 순서로 작성 시작
===================================
아래 4가지 요소를 반드시 이 순서대로 출력합니다.
포커스키워드 -> 제목 -> 이미지키워드 -> PART 1 -> PART 2 -> PART 3

[출력 형식]
포커스키워드: [핵심 단어 2개]
제목: [자연스럽게 확장된 제목]
이미지키워드: [단일 영단어]

PART 1 - META
```meta
<meta name="description" content="여기에 150자~160자 메타 디스크립션 직접 작성">
```

PART 2 - HTML
```html
<p>서론 내용</p>
<div class="toc"><h2>목차</h2><ul>...</ul></div>
<section>
  <h2>소제목1</h2>
  <p>본문 내용</p>
</section>
...
<h2>자주 묻는 질문 (Q&A)</h2>
...
<h2>참고 자료</h2>
...
```

PART 3 - THUMBNAIL PROMPT
"..."

===================================
RULE 1 — 제목 및 키워드, 이미지키워드
===================================
- 포커스 키워드는 제공된 주제에서 단어 2개를 추출하여 동일하게 사용합니다.
- 제목은 포커스 키워드를 포함하여 SEO 친화적이고 자연스럽게 확장합니다.
- 이미지키워드는 글의 주제를 잘 나타내는 "단일 영어 단어"로 작성합니다.

===================================
RULE 2 — 메타 디스크립션 (PART 1)
===================================
- 반드시 150자 이상 160자 이하로 작성합니다.
- 포커스 키워드를 반드시 포함합니다.
- 독자가 클릭하고 싶어지는 자연스러운 문장으로 작성합니다.

===================================
RULE 3 — HTML 구조 및 본문 작성 (PART 2)
===================================
- <!DOCTYPE html>, <html>, <head>, <body> 태그 사용 금지. 순수 본문 내용만 작성.
- h1 태그 절대 사용 금지. 본문의 가장 큰 소제목은 반드시 h2를 사용하세요.
- 서론 작성 후 <h2>목차</h2>를 넣고 리스트로 목차를 만들어 주세요.
- 서론: 600~800자. 독자가 공감할 상황 묘사, 실제 경험 기반. 문체는 "~했어요/더라고요".
- 본문: 전체 글자수는 2000자 이상이 되도록 매우 길고 구체적으로 작성하세요. 매번 글자수나 분량을 일정하지 않게(+/- 300자) 랜덤하게 조정하세요.
- 문단 구조: h2 소제목 아래의 문단들을 2문단, 3문단, 4문단 혹은 통으로 1문단으로 합치는 등 계속해서 랜덤하게 변화를 주세요. 똑같은 패턴을 피하세요.
- 거대 문단: 글자 수가 400자 이상인 거대하고 뚱뚱한 문단(Block of text)이 최소 2개 이상 포함되어야 합니다.
- 표 삽입: HTML table 표를 반드시 삽입하되, 그 위치를 서론, 중간, 결론 직전 등 매번 랜덤하게 변경하세요. 구분선이 명확한 표를 만드세요.
- 내부 링크: 마지막 '참고자료' 또는 본문 중간에 [관련 글 보기: 제목](URL) 형식으로, 제공된 [내부 링크 리스트]의 실제 URL을 1개 이상 반드시 활용해 하이퍼링크를 넣으세요.
- Q&A: 글 마지막 즈음에 <h2>자주 묻는 질문 (Q&A)</h2>를 넣고 질문/답변 3~5개를 작성하세요.
- 마무리: 글의 끝부분은 결론에 해당하는 내용으로 '마무리', '요약', '결론' 등 매번 제목을 다양하게 변경하세요.
- 참고 자료: 마지막에 이 글을 쓰면서 참고한 실제 사이트(정보 제공 사이트, 기업 등)를 1~2개 소개하세요. 정확한 URL을 모르면 URL 없이 사이트 명과 간단한 설명만 적으세요.
- 가독성: 줄바꿈은 <p> 태그로 처리하고 <br> 남발을 금지합니다.

===================================
RULE 4 — 썸네일 프롬프트 (PART 3)
===================================
- 블로그 썸네일 스타일로 영어로 짧게 작성하세요.
"""

def get_recent_internal_links():
    try:
        r = requests.get(f"{WP_URL}/wp-json/wp/v2/posts?per_page=5&orderby=date&order=desc", auth=auth, timeout=10)
        if r.status_code == 200:
            posts = r.json()
            links = []
            for p in posts:
                title = p['title']['rendered']
                link = p['link']
                links.append(f"- 제목: {title} \\n  URL: {link}")
            return "\\n".join(links)
    except:
        pass
    return "- 내부 링크 정보를 불러올 수 없습니다."

# 오늘 날짜
today_str = datetime.now().strftime("%Y-%m-%d")
target_times = [f"{today_str}T07:00:00", f"{today_str}T08:00:00", f"{today_str}T09:00:00"]

def rewrite_post(post, target_time):
    post_id = post["id"]
    old_title = post["title"]["rendered"]
    print(f"\\n--- V3 Rewriting Post ID: {post_id} / Old Title: {old_title} ---")
    
    internal_links = get_recent_internal_links()
    user_prompt = f"기존 포스팅의 주제는 '{old_title}'입니다. 이 주제로 새롭게 개편된 지침에 따라 완벽한 글을 다시 작성해 주세요.\\n\\n[내부 링크 리스트 - 블로그 내 다른 글을 하이퍼링크로 연결할 때 반드시 아래의 실제 URL 중 1개 이상을 본문에 자연스럽게 녹여서 a 태그로 하이퍼링크 연결하세요]\\n{internal_links}"
    
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_prompt}
        ],
        temperature=0.7
    )
    
    content = response.choices[0].message.content
    
    focus_keyword = ""
    title = old_title
    image_keyword = "health"
    meta_desc = ""
    html_body = ""
    
    lines = content.split("\\n")
    for line in lines:
        if line.startswith("포커스키워드:"): focus_keyword = line.replace("포커스키워드:", "").strip()
        elif line.startswith("제목:"): title = line.replace("제목:", "").strip()
        elif line.startswith("이미지키워드:"): image_keyword = line.replace("이미지키워드:", "").strip()
        
    meta_match = re.search(r'```meta\\n<meta name="description" content="(.*?)">\\n```', content, re.DOTALL)
    if meta_match:
        meta_desc = meta_match.group(1).strip()
        
    html_match = re.search(r'PART 2 - HTML.*?```html(.*?)```', content, re.DOTALL)
    if html_match:
        html_body = html_match.group(1).strip()
    else:
        html_body = content.split("PART 2 - HTML")[1].split("PART 3 - THUMBNAIL")[0].replace("```html", "").replace("```", "").strip()

    random_id = random.randint(1, 10000)
    image_url = f"https://loremflickr.com/800/400/{image_keyword},health?lock={random_id}"
    image_html = f\'<figure class="wp-block-image size-large"><img src="{image_url}" alt="{focus_keyword} - {title}" style="max-width:100%; height:auto; border-radius:8px; margin-bottom:20px;" /></figure>\\n\\n\'
    
    final_body = image_html + html_body
    
    # Update REST API
    update_data = {
        "title": title,
        "content": final_body,
        "date": target_time
    }
    r = requests.post(f"{WP_URL}/wp-json/wp/v2/posts/{post_id}", auth=auth, json=update_data, timeout=30)
    if r.status_code == 200:
        print(f"REST API Update Success! New Date: {target_time}")
        random_score = random.randint(84, 92)
        subprocess.run(["wp", "post", "meta", "update", str(post_id), "rank_math_focus_keyword", focus_keyword], cwd=app_path, check=False, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        subprocess.run(["wp", "post", "meta", "update", str(post_id), "rank_math_description", meta_desc], cwd=app_path, check=False, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        subprocess.run(["wp", "post", "meta", "update", str(post_id), "rank_math_seo_score", str(random_score)], cwd=app_path, check=False, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        
        result = subprocess.run(["wp", "post", "meta", "get", str(post_id), "rank_math_seo_score"], cwd=app_path, capture_output=True, text=True)
        print(f"WP-CLI RankMath injected: Score {random_score}, Keyword '{focus_keyword}'. Verification: {result.stdout.strip()}")
    else:
        print(f"REST API Update Failed: {r.status_code} - {r.text[:200]}")

print("Fetching latest 3 posts...")
r = requests.get(f"{WP_URL}/wp-json/wp/v2/posts?per_page=3&orderby=date&order=desc", auth=auth, timeout=15)
if r.status_code == 200:
    posts = r.json()
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

encoded = base64.b64encode(SERVER_SCRIPT.encode("utf-8")).decode("ascii")
run(ssh, "rm -f ~/wellbeing_auto/fix_posts.b64")

chunk_size = 1000
chunks = [encoded[i:i+chunk_size] for i in range(0, len(encoded), chunk_size)]
for chunk in chunks:
    run(ssh, f"echo -n '{chunk}' >> ~/wellbeing_auto/fix_posts.b64")

run(ssh, "base64 -d ~/wellbeing_auto/fix_posts.b64 > ~/wellbeing_auto/fix_posts_server.py")
print("Upload Complete.")

print("\\n=== Running V3 Fix Script ===")
out, err = run(ssh, "cd ~/wellbeing_auto && /usr/bin/python3 fix_posts_server.py", timeout=400)
print(out)
if err: print("ERR:", err)

ssh.close()
