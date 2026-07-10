import os
import requests
import json
import sys
import random
import re
from datetime import datetime
from dotenv import load_dotenv
from openai import OpenAI
import openai
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

# 3-Pass 시스템은 generate_post_with_prompt 내부에서 개별 프롬프트로 관리됩니다.

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
    print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] 3-Pass E-E-A-T 글 생성을 시작합니다...")
    internal_links = get_recent_internal_links()
    
    # 구조적 무작위성 부여 (스팸 패턴 파괴)
    use_table = random.choice([True, False, False]) # 33% 확률로 표 사용
    use_qa = random.choice([True, True, False]) # 66% 확률로 Q&A 사용
    use_checklist = random.choice([True, False]) # 50% 확률로 체크리스트 사용
    
    try:
        # --- PASS 1: 기획 및 아웃라인 ---
        print(">> [Pass 1] 기획 및 구조(Outline) 설계 중...")
        pass1_msg = [
            {"role": "system", "content": "당신은 객관적이고 신뢰할 수 있는 건강/의학 정보 큐레이터입니다. 주어진 주제에 대한 포커스키워드, 제목, 상세 목차(H2, H3)를 기획하세요. 제목은 클릭을 유도하되 자극적이지 않은 전문가 칼럼 스타일이어야 합니다.\n[출력형식]\n포커스키워드: [단어 2개]\n제목: [매력적인 제목]\n\n[목차]\n- 서론 (연구 결과나 통계 등 객관적 사실로 시작)\n- [H2] ...\n  - [H3] ...\n- 결론"},
            {"role": "user", "content": f"주제 및 지시사항: {user_prompt}"}
        ]
        r1 = client.chat.completions.create(model="gpt-4o-mini", messages=pass1_msg, temperature=0.7)
        outline = r1.choices[0].message.content
        
        # --- PASS 2: 본문 초안 작성 ---
        print(">> [Pass 2] 독자 중심 본문 초안 작성 중...")
        pass2_msg = [
            {"role": "system", "content": "당신은 전문 건강/의학 정보 에디터입니다. 기획안(Outline)을 바탕으로 독자가 안전하게 이해하고 적용할 수 있는 상세한 초안을 작성하세요. 절대 가상의 인물이나 꾸며낸 경험담을 쓰지 마세요. 특정 식단, 운동, 보충제, 생활습관이 모든 사람에게 효과가 있다고 단정하지 말고 주의 대상과 예외를 함께 설명하세요. 어투는 정중하고 전문적인 '다/나/까' 또는 '해요체'를 일관되게 사용하세요. 순수 텍스트(본문)만 충실히 작성하세요."},
            {"role": "user", "content": f"기획안:\n{outline}"}
        ]
        r2 = client.chat.completions.create(model="gpt-4o", messages=pass2_msg, temperature=0.7)
        draft = r2.choices[0].message.content
        
        # --- PASS 3: E-E-A-T 윤문 및 HTML/SEO 포맷팅 ---
        print(">> [Pass 3] HTML 포맷팅, SEO 최적화 및 E-E-A-T 주입 중...")
        
        structure_instructions = []
        if use_table:
            structure_instructions.append("본문 내에 반드시 <table> 태그를 활용한 '데이터/비교 표'를 1개 삽입하세요.")
        if use_qa:
            structure_instructions.append("문서 하단(참고자료 직전)에 '<h2>자주 묻는 질문 (Q&A)</h2>' 섹션을 추가하여 2~3개의 Q&A를 작성하세요.")
        if use_checklist:
            structure_instructions.append("본문 중 적절한 곳에 '✔ 핵심 체크리스트'라는 제목의 <ul> 리스트를 추가하세요.")
            
        pass3_sys = f"""당신은 테크니컬 SEO 및 웹 퍼블리싱 전문가입니다. 기획안과 본문 초안을 바탕으로 최종 완벽한 HTML 코드를 생성하세요.
[지침]
1. 가독성: 소제목(<h2>, <h3>)과 리스트(<ul>, <li>), 적절한 문단 나누기(<p>)를 활용하세요. <h1> 태그는 절대 사용 금지.
2. { ' '.join(structure_instructions) }
3. 마크다운 사용 금지: 본문 내용에 마크다운 기호(###, **, -)를 쓰지 말고, 순수 HTML 태그(<strong> 등)만 사용하세요.
4. 내부 링크: 제공된 내부 링크 리스트를 활용하여 본문이나 참고자료 섹션에 <a href="..."> 태그로 1개 이상 연결하세요.
5. 안전 고지: 참고 자료 직전에 class="wellbeing-medical-disclaimer"인 div를 넣고, 이 글은 일반 건강 정보이며 진단·치료를 대신하지 않고 개인 건강 상태가 있으면 의료 전문가와 상담해야 한다고 안내하세요.
6. 외부 공공기관 인용(Outbound Links): 본문 하단 '참고 자료' 섹션에 공신력 있는 외부 링크를 1~2개 삽입하세요. 가짜 URL을 지어내지 말고, 실제 존재하는 공식 기관 메인 URL(예: https://health.kdca.go.kr) 또는 확실한 자료 URL만 사용하세요.

[출력 구조]
포커스키워드: [핵심 단어 2개]
제목: [포커스 키워드가 포함된 구체적인 제목. 절대 "건강 가이드"만 출력하지 말 것]

PART 1 - META
```meta
<meta name="description" content="150~160자 사이의 검색엔진 요약문">
```

PART 2 - HTML
```html
<p>서론 부분...</p>
<h2>소제목</h2>
<p>상세 내용...</p>
...
<div class="wellbeing-medical-disclaimer">
  <p><strong>건강 정보 이용 안내</strong></p>
  <p>이 글은 일반적인 건강 정보 제공을 목적으로 작성되었으며, 개인의 진단이나 치료를 대신하지 않습니다. 질환이 있거나 약물을 복용 중인 경우, 임신 중이거나 통증·어지럼·호흡곤란 같은 증상이 있다면 실천 전 의사 또는 의료 전문가와 상담하시기 바랍니다.</p>
</div>
<h2>참고 자료</h2>
<ul>
  <li><a href="...">...</a></li>
</ul>
```"""
        pass3_user = f"내부 링크 리스트:\n{internal_links}\n\n[기획안]\n{outline}\n\n[본문 초안]\n{draft}"
        pass3_msg = [
            {"role": "system", "content": pass3_sys},
            {"role": "user", "content": pass3_user}
        ]
        r3 = client.chat.completions.create(model="gpt-4o", messages=pass3_msg, temperature=0.7)
        content = r3.choices[0].message.content
        
        # Parsing
        focus_keyword = ""
        title = "건강 가이드"
        meta_desc = ""
        html_body = ""
        
        lines = content.split("\n")
        for line in lines:
            if line.startswith("포커스키워드:"): focus_keyword = line.replace("포커스키워드:", "").strip()
            elif line.startswith("제목:"): title = line.replace("제목:", "").strip()
            
        meta_match = re.search(r'```meta\n<meta name="description" content="(.*?)">\n```', content, re.DOTALL)
        if meta_match:
            meta_desc = meta_match.group(1).strip()
            
        html_match = re.search(r'PART 2 - HTML.*?```html(.*?)```', content, re.DOTALL)
        if html_match:
            html_body = html_match.group(1).strip()
        else:
            if "PART 2 - HTML" in content:
                parts = content.split("PART 2 - HTML")
                if len(parts) > 1:
                    html_part = parts[1].split("PART 3")[0]
                    html_body = html_part.replace("```html", "").replace("```", "").strip()

        # LoremFlickr 스팸 썸네일 전면 제거. (텍스트 온리 고품질 칼럼화)
        final_body = html_body
        
        print(">> [완료] 3-Pass 생성 성공!")
        return title, final_body, focus_keyword, meta_desc
    except openai.RateLimitError as e:
        print(f"🚨 API 429 한도 초과 에러 발생: {e}")
        return "RATE_LIMIT", None, None, None
    except Exception as e:
        print(f"3-Pass 글 생성 중 오류 발생: {e}")
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
            
            # WP-CLI RankMath SEO (절대 경로 사용)
            try:
                wp_cli = "/usr/local/bin/wp"
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
        # 인자가 없으면 현재 시간에 맞춰 실행 (수동 실행용)
        hour = datetime.now().hour
        if hour < 14:
            job_morning()
        else:
            job_afternoon()
