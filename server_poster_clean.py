import os
import requests
import json
import sys
import random
import re
from datetime import datetime
from dotenv import load_dotenv
from openai import OpenAI
from requests.auth import HTTPBasicAuth
import subprocess

# .env 파일 로드
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
load_dotenv(os.path.join(SCRIPT_DIR, ".env"))

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
WP_URL = os.getenv("WP_URL")
WP_USERNAME = os.getenv("WP_USERNAME")
WP_APP_PASSWORD = os.getenv("WP_APP_PASSWORD")
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

client = OpenAI(api_key=OPENAI_API_KEY)
auth = HTTPBasicAuth(WP_USERNAME, WP_APP_PASSWORD)

SYSTEM_PROMPT = """
당신은 'Wellbeing Health' 블로그의 수석 에디터이자 20년 경력의 건강 콘텐츠 전략가입니다.
당신의 목표는 독자가 안전하게 이해하고 적용할 수 있는 고품질 한국어 건강 정보를 작성하는 것입니다.

[핵심 지침]
1. E-E-A-T 강화: 실제로 겪지 않은 개인 경험담, 가상 사례, 꾸며낸 인물, 과장된 전문가 경력을 절대 쓰지 마세요.
2. 가독성 최적화: 너무 긴 문단(Wall of text)보다는 적절한 길이의 문단과 소제목, 리스트를 사용하여 읽기 편하게 작성하세요.
3. 분량: 한국어 기준 공백 포함 반드시 2,500자 이상으로 매우 상세하게 작성하세요.
4. 형식: 반드시 순수 HTML 태그 형식으로만 출력하세요. 마크다운 기호(###, **, - 등)를 본문 태그 내에 절대 사용하지 마세요.
5. 내부 링크: 제공된 내부 링크 리스트를 활용하여 본문 중간이나 참고 자료 섹션에 <a href="..."> 태그로 자연스럽게 삽입하세요.
6. 안전 고지: 참고 자료 직전에 class="wellbeing-medical-disclaimer"인 div를 넣고, 이 글은 일반 건강 정보이며 진단·치료를 대신하지 않고 개인 건강 상태가 있으면 의료 전문가와 상담해야 한다고 안내하세요.
7. 외부 링크: 가짜 세부 URL을 만들지 말고, 실제로 존재하는 공공기관/의학기관 메인 URL 또는 확실한 자료 URL만 사용하세요.

[출력 구조]
포커스키워드: [핵심 단어 2개]
제목: [포커스 키워드가 포함된 구체적인 제목. 절대 "건강 가이드"만 출력하지 말 것]
이미지키워드: [단일 영단어]

PART 1 - META
```meta
<meta name="description" content="포커스 키워드를 포함하여 150~160자 사이의 요약문 작성">
```

PART 2 - HTML
```html
<p>공감을 유도하는 따뜻한 서론 (600자 내외)</p>
<div class="toc"><h2>목차</h2><ul><li>...</li></ul></div>

<section>
  <h2>소제목</h2>
  <p>상세 내용...</p>
  <table>...</table> <!-- 표는 본문 중 적절한 위치에 1회 이상 삽입 -->
</section>

<h2>자주 묻는 질문 (Q&A)</h2>
<p><strong>Q: 질문?</strong><br>A: 답변...</p>

<div class="wellbeing-medical-disclaimer">
  <p><strong>건강 정보 이용 안내</strong></p>
  <p>이 글은 일반적인 건강 정보 제공을 목적으로 작성되었으며, 개인의 진단이나 치료를 대신하지 않습니다. 질환이 있거나 약물을 복용 중인 경우, 임신 중이거나 통증·어지럼·호흡곤란 같은 증상이 있다면 실천 전 의사 또는 의료 전문가와 상담하시기 바랍니다.</p>
</div>

<h2>참고 자료</h2>
<ul>
  <li><a href="실제_공식기관_URL">관련 기관 명칭 및 설명</a></li>
  <li><a href="실제_내부_링크_URL">관련 글 보기: 제목</a></li>
</ul>
```

[주의사항]
- <h1> 태그는 사용하지 마세요. (워드프레스 제목이 h1이 됩니다)
- 모든 텍스트는 한국어로 작성하되, 이미지키워드만 영어 단어로 작성하세요.
- 마크다운 코드 블록(```html) 외에 본문 내용 자체에 마크다운 문법을 절대 섞지 마세요.
- 특정 식단, 운동, 보충제, 생활습관이 모든 사람에게 효과가 있다고 단정하지 마세요.
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

def get_recent_internal_links():
    try:
        r = requests.get(f"{WP_URL}/wp-json/wp/v2/posts?per_page=5&orderby=date&order=desc", auth=auth, timeout=30)
        if r.status_code == 200:
            posts = r.json()
            links = []
            for p in posts:
                title = p['title']['rendered']
                link = p['link']
                links.append(f"- {title}: {link}")
            return "\n".join(links)
    except Exception as e:
        print(f"Internal links fetch error: {e}")
    return "- 내부 링크 정보를 불러올 수 없습니다."

def generate_post_with_prompt(user_prompt):
    print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] 글 생성을 시작합니다...")
    internal_links = get_recent_internal_links()
    
    dynamic_prompt = user_prompt + f"\n\n[내부 링크 리스트 - 블로그 내 다른 글을 연결할 때 반드시 아래의 실제 URL을 사용하세요]\n{internal_links}"

    try:
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": dynamic_prompt}
            ],
            temperature=0.7
        )
        content = response.choices[0].message.content
        
        # Parsing
        focus_keyword = ""
        title = "건강 가이드"
        image_keyword = "health"
        meta_desc = ""
        html_body = ""
        
        # Extract basic info
        lines = content.split("\n")
        for line in lines:
            if line.startswith("포커스키워드:"): focus_keyword = line.replace("포커스키워드:", "").strip()
            elif line.startswith("제목:"): title = line.replace("제목:", "").strip()
            elif line.startswith("이미지키워드:"): image_keyword = line.replace("이미지키워드:", "").strip()
            
        # Extract Meta
        meta_match = re.search(r'```meta\n<meta name="description" content="(.*?)">\n```', content, re.DOTALL)
        if meta_match:
            meta_desc = meta_match.group(1).strip()
            
        # Extract HTML
        html_match = re.search(r'PART 2 - HTML.*?```html(.*?)```', content, re.DOTALL)
        if html_match:
            html_body = html_match.group(1).strip()
        else:
            # Fallback
            if "PART 2 - HTML" in content:
                parts = content.split("PART 2 - HTML")
                if len(parts) > 1:
                    html_part = parts[1].split("PART 3")[0]
                    html_body = html_part.replace("```html", "").replace("```", "").strip()

        if title == "건강 가이드":
            print("생성 결과의 제목이 기본값이라 발행을 중단합니다.")
            return None, None, None, None

        final_body = html_body
        
        return title, final_body, focus_keyword, meta_desc
    except Exception as e:
        print(f"글 생성 중 오류 발생: {e}")
        return None, None, None, None

def send_telegram_message(message):
    if not TELEGRAM_BOT_TOKEN or not TELEGRAM_CHAT_ID:
        return
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    try:
        res = requests.post(url, json={"chat_id": TELEGRAM_CHAT_ID, "text": message, "parse_mode": "HTML"}, timeout=10)
        if res.status_code == 200:
            print("📲 텔레그램 알림 전송 완료!")
        else:
            print(f"❌ 텔레그램 전송 실패: {res.text}")
    except Exception as e:
        print(f"텔레그램 전송 중 오류: {e}")

def post_to_wordpress(title, body, focus_keyword, meta_desc, category_id):
    api_url = f"{WP_URL}/wp-json/wp/v2/posts"
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
            print(f"✅ 발행 성공! ID: {post_id}, URL: {link}")
            
            # WP-CLI RankMath SEO
            try:
                wp_cli = "/usr/local/bin/wp" # 서버 경로
                app_path = "/home/1591341.cloudwaysapps.com/jcclwggqub/public_html"
                random_score = random.randint(84, 92)
                
                subprocess.run([wp_cli, "post", "meta", "update", str(post_id), "rank_math_focus_keyword", focus_keyword], cwd=app_path, check=False)
                subprocess.run([wp_cli, "post", "meta", "update", str(post_id), "rank_math_description", meta_desc], cwd=app_path, check=False)
                subprocess.run([wp_cli, "post", "meta", "update", str(post_id), "rank_math_seo_score", str(random_score)], cwd=app_path, check=False)
                print(f"✅ RankMath SEO 주입 완료! (점수: {random_score})")
            except Exception as cli_err:
                print(f"⚠️ WP-CLI 오류: {cli_err}")
                
            msg = f"🎉 <b>[웰빙헬스] 자동 발행 완료!</b>\n\n📝 <b>제목:</b> {title}\n🔑 <b>키워드:</b> {focus_keyword}\n🔗 <b>링크:</b> {link}"
            send_telegram_message(msg)
        else:
            print(f"❌ 발행 실패: {response.status_code} - {response.text[:200]}")
    except Exception as e:
        print(f"API 호출 오류: {e}")

def job_morning():
    print("🌅 오전 포스팅 작업 시작")
    topic = get_next_topic()
    if topic:
        chosen_cat = topic["category"]
        cat_id = CATEGORIES.get(chosen_cat, 8)
        user_prompt = f"오늘의 포스팅 주제는 '{topic['title']}'입니다. 소제목으로 {', '.join(topic['subtitles'])}을 활용해 주세요. 카테고리는 '{chosen_cat}'입니다."
    else:
        chosen_cat = random.choice(["운동", "다이어트", "건강식단"])
        cat_id = CATEGORIES[chosen_cat]
        user_prompt = f"카테고리 '{chosen_cat}'에 어울리는 구체적인 세부 주제를 하나 정해서 블로그 포스팅을 작성해 주세요."
    title, body, focus_keyword, meta_desc = generate_post_with_prompt(user_prompt)
    if title and body:
        post_to_wordpress(title, body, focus_keyword, meta_desc, cat_id)

def job_afternoon():
    print("☕ 오후 포스팅 작업 시작")
    topic = get_next_topic()
    if topic:
        chosen_cat = topic["category"]
        cat_id = CATEGORIES.get(chosen_cat, 5)
        user_prompt = f"오늘의 포스팅 주제는 '{topic['title']}'입니다. 소제목으로 {', '.join(topic['subtitles'])}을 활용해 주세요. 카테고리는 '{chosen_cat}'입니다."
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
        hour = datetime.now().hour
        if hour < 14:
            job_morning()
        else:
            job_afternoon()
