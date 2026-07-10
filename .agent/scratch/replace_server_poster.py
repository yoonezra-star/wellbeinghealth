import paramiko
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

hostname = "129.212.235.171"
username = "master_zmuwemtfup"
password = "VjdUUR4pRsTj"

# 완전히 새로 작성한 서버용 server_poster.py
NEW_SERVER_POSTER = '''import os
import requests
import json
import sys
import random
from datetime import datetime
from dotenv import load_dotenv
from openai import OpenAI
from requests.auth import HTTPBasicAuth

# .env 파일 로드 (절대 경로 사용 - 크론잡 환경 대응)
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
load_dotenv(os.path.join(SCRIPT_DIR, ".env"))

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
WP_URL = os.getenv("WP_URL")
WP_USERNAME = os.getenv("WP_USERNAME")
WP_APP_PASSWORD = os.getenv("WP_APP_PASSWORD")
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

client = OpenAI(api_key=OPENAI_API_KEY)

SYSTEM_PROMPT = """
당신은 'Wellbeing Health' 블로그의 수석 에디터이자 10년 차 건강/멘탈케어 전문가인 '웰빙코치'입니다.
독자들이 실생활에서 바로 적용할 수 있는 구체적이고 실용적인 건강, 식단, 다이어트, 멘탈케어 가이드를 작성하세요.

[작성 규칙]
1. 화자는 '저(웰빙코치)', 독자는 '여러분'. 친근하고 전문적인 경어체.
2. 독특하고 세부적인 개인적 경험담(가상)으로 시작.
3. 서론 직후 <h2>목차</h2>와 <ul><li> 로 소제목 나열.
4. <h2>, <h3>, <p> 태그로 구조화. HTML table 1개 이상 삽입.
5. 글 마지막 <h2>참고 자료</h2>에 외부 링크 1~2개, 내부 링크 1개.
6. 전체 3,500자 이상. 포커스 키워드를 본문 첫 문장 첫 단어로 배치.

[출력 형식]
포커스키워드: [핵심 키워드 1개]
메타디스크립션: [160자 이내 요약]
제목: [포스팅 제목]
이미지키워드: [단일 영단어]
본문:
[HTML 태그 형식 본문]
"""

CATEGORIES = {
    "운동": 3,
    "다이어트": 4,
    "건강식단": 8,
    "생활습관": 5,
    "멘탈케어": 6,
    "전문가칼럼": 7
}

QUEUE_FILE = os.path.join(SCRIPT_DIR, "topic_queue.json")

def get_next_topic():
    if not os.path.exists(QUEUE_FILE):
        return None
    try:
        with open(QUEUE_FILE, "r", encoding="utf-8") as f:
            queue = json.load(f)
        if not queue:
            return None
        topic = queue.pop(0)
        with open(QUEUE_FILE, "w", encoding="utf-8") as f:
            json.dump(queue, f, ensure_ascii=False, indent=4)
        return topic
    except Exception as e:
        print(f"Queue load error: {e}")
        return None

def generate_post_with_prompt(user_prompt):
    print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Generating post...")
    try:
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
        focus_keyword, meta_desc, title, image_keyword = "", "", "건강 가이드", "health"
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
        return title, image_html + raw_body, focus_keyword, meta_desc
    except Exception as e:
        print(f"Post generation error: {e}")
        return None, None, None, None

def send_telegram_message(message):
    if not TELEGRAM_BOT_TOKEN or not TELEGRAM_CHAT_ID:
        return
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    try:
        requests.post(url, json={"chat_id": TELEGRAM_CHAT_ID, "text": message, "parse_mode": "HTML"}, timeout=10)
    except:
        pass

def post_to_wordpress(title, body, focus_keyword, meta_desc, category_id):
    api_url = f"{WP_URL}/wp-json/wp/v2/posts"
    auth = HTTPBasicAuth(WP_USERNAME, WP_APP_PASSWORD)
    post_data = {
        "title": title,
        "content": body,
        "status": "publish",
        "categories": [category_id],
        "meta": {
            "rank_math_focus_keyword": focus_keyword,
            "rank_math_description": meta_desc,
            "rank_math_title": title
        }
    }
    try:
        response = requests.post(api_url, auth=auth, json=post_data, timeout=30)
        if response.status_code == 201:
            res_json = response.json()
            link = res_json.get("link")
            post_id = res_json.get("id")
            print(f"SUCCESS! ID: {post_id}, URL: {link}")
            msg = f"[Wellbeing Health] 자동 발행 완료\\n제목: {title}\\n키워드: {focus_keyword}\\n링크: {link}"
            send_telegram_message(msg)
        else:
            print(f"FAILED: {response.status_code} - {response.text[:200]}")
    except Exception as e:
        print(f"API error: {e}")

def job_morning():
    print("MORNING POST START")
    topic = get_next_topic()
    if topic:
        chosen_cat = topic["category"]
        cat_id = CATEGORIES.get(chosen_cat, 8)
        user_prompt = f"오늘의 포스팅 주제는 '{topic['title']}'입니다. 소제목으로 {', '.join(topic['subtitles'])}을 반드시 포함하여 작성해 주세요. 카테고리는 '{chosen_cat}'입니다."
    else:
        chosen_cat = random.choice(["운동", "다이어트", "건강식단"])
        cat_id = CATEGORIES[chosen_cat]
        user_prompt = f"카테고리 '{chosen_cat}'에 어울리는 구체적인 세부 주제를 하나 정해서 블로그 포스팅을 작성해 주세요."
    title, body, focus_keyword, meta_desc = generate_post_with_prompt(user_prompt)
    if title and body:
        post_to_wordpress(title, body, focus_keyword, meta_desc, cat_id)

def job_afternoon():
    print("AFTERNOON POST START")
    topic = get_next_topic()
    if topic:
        chosen_cat = topic["category"]
        cat_id = CATEGORIES.get(chosen_cat, 5)
        user_prompt = f"오늘의 포스팅 주제는 '{topic['title']}'입니다. 소제목으로 {', '.join(topic['subtitles'])}을 반드시 포함하여 작성해 주세요. 카테고리는 '{chosen_cat}'입니다."
    else:
        chosen_cat = random.choice(["생활습관", "멘탈케어"])
        cat_id = CATEGORIES[chosen_cat]
        user_prompt = f"카테고리 '{chosen_cat}'에 어울리는 구체적인 세부 주제를 하나 정해서 블로그 포스팅을 작성해 주세요."
    title, body, focus_keyword, meta_desc = generate_post_with_prompt(user_prompt)
    if title and body:
        post_to_wordpress(title, body, focus_keyword, meta_desc, cat_id)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        arg = sys.argv[1]
        if arg == "morning":
            job_morning()
        elif arg == "afternoon":
            job_afternoon()
        else:
            print("Usage: python3 server_poster.py [morning|afternoon]")
    else:
        print("Usage: python3 server_poster.py [morning|afternoon]")
'''

def run(ssh, cmd, timeout=30):
    stdin, stdout, stderr = ssh.exec_command(cmd, timeout=timeout)
    out = stdout.read().decode("utf-8", errors="replace").strip()
    err = stderr.read().decode("utf-8", errors="replace").strip()
    return out, err

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname, username=username, password=password)
print("SSH Connected OK")

# 백업 후 새 파일 업로드
print("\n=== Backing up old server_poster.py ===")
out, err = run(ssh, "cp ~/wellbeing_auto/server_poster.py ~/wellbeing_auto/server_poster.py.bak")
print("Backup OK" if not err else f"ERR: {err}")

print("\n=== Uploading new server_poster.py ===")
sftp = ssh.open_sftp()
with sftp.open('/home/master/wellbeing_auto/server_poster.py', 'w') as f:
    f.write(NEW_SERVER_POSTER)
sftp.close()
print("Upload complete")

print("\n=== SYNTAX CHECK ===")
out, err = run(ssh, "cd ~/wellbeing_auto && /usr/bin/python3 -m py_compile server_poster.py && echo 'SYNTAX: OK'")
print(out)
if err and 'Error' in err: print("ERR:", err)

print("\n=== QUICK IMPORT TEST ===")
out, err = run(ssh, "cd ~/wellbeing_auto && /usr/bin/python3 server_poster.py 2>&1")
print("OUT:", out)
if err: print("ERR:", err)

print("\n=== First 15 lines of new file ===")
out, _ = run(ssh, "head -15 ~/wellbeing_auto/server_poster.py")
print(out)

ssh.close()
print("\n=== Done ===")
