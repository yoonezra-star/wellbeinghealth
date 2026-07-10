"""
auto_poster_static.py
=====================
GPT로 글을 생성하고 Markdown 파일로 저장한 뒤
git commit + push → Cloudflare Pages 자동 배포

사용법:
  python auto_poster_static.py
"""

import os
import re
import time
import random
import subprocess
import requests
from datetime import datetime
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")
GITHUB_REPO_PATH = os.getenv("GITHUB_REPO_PATH", os.path.dirname(os.path.abspath(__file__)))
POSTS_DIR = os.path.join(GITHUB_REPO_PATH, "site", "content", "posts")

client = OpenAI(api_key=OPENAI_API_KEY)

SYSTEM_PROMPT = """
당신은 'Wellbeing Health' 블로그의 건강 정보 에디터입니다.
독자들이 실생활에서 안전하게 참고할 수 있는 구체적이고 실용적인 건강, 식단, 다이어트, 멘탈케어 정보를 작성합니다.

[작성 규칙]
1. 화자는 '저(웰빙코치)', 독자는 '여러분'. 친근하고 전문적인 경어체.
2. 서론: 주제와 핵심 기준을 명확히 제시. 가상 경험담 금지.
3. 목차: 서론 직후 ## 목차 작성, 본문 소제목 나열.
4. 본문: ## ### 소제목 구조화, 독창적인 꿀팁과 액션 플랜.
5. 반드시 마크다운 표(|col|col|) 1개 이상 포함.
6. 결론에 공신력 있는 외부 링크 1~2개, Wellbeing Health 내부 링크 1개.
7. 전체 3,500자 이상.
8. 포커스 키워드를 본문 첫 문장 첫 단어/구절로 배치.

[출력 형식 - 반드시 준수]
포커스키워드: [키워드]
메타디스크립션: [160자 이내]
제목: [포스팅 제목]
슬러그: [영문-소문자-하이픈 형식, 예: intermittent-fasting-guide]
카테고리: [운동|다이어트|건강식단|생활습관|멘탈케어|전문가칼럼 중 하나]
본문:
[여기서부터 마크다운 형식의 본문]
"""

CATEGORIES = ["운동", "다이어트", "건강식단", "생활습관", "멘탈케어", "전문가칼럼"]

QUEUE_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "topic_queue.json")


def get_next_topic():
    import json
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
        print(f"큐 로드 오류: {e}")
        return None


def generate_post(user_prompt: str):
    print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] 글 생성 시작...")
    try:
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": user_prompt},
            ],
            temperature=0.7,
        )
        content = response.choices[0].message.content
        lines = content.split("\n")

        focus_keyword = ""
        meta_desc = ""
        title = ""
        slug = ""
        category = "건강식단"
        body_lines = []
        is_body = False

        for line in lines:
            if line.startswith("포커스키워드:"):
                focus_keyword = line.replace("포커스키워드:", "").strip()
            elif line.startswith("메타디스크립션:"):
                meta_desc = line.replace("메타디스크립션:", "").strip()
            elif line.startswith("제목:"):
                title = line.replace("제목:", "").strip()
            elif line.startswith("슬러그:"):
                slug = line.replace("슬러그:", "").strip()
            elif line.startswith("카테고리:"):
                category = line.replace("카테고리:", "").strip()
            elif line.startswith("본문:"):
                is_body = True
            elif is_body:
                body_lines.append(line)

        body = "\n".join(body_lines).strip()

        if not title:
            print("제목 파싱 실패, 발행 중단.")
            return None

        # 슬러그 자동 생성 (없는 경우)
        if not slug:
            slug = re.sub(r"[^a-z0-9]+", "-", focus_keyword.lower()).strip("-")
            if not slug:
                slug = f"post-{datetime.now().strftime('%Y%m%d%H%M%S')}"

        return {
            "title": title,
            "slug": slug,
            "category": category,
            "focus_keyword": focus_keyword,
            "meta_desc": meta_desc,
            "body": body,
        }

    except Exception as e:
        print(f"글 생성 오류: {e}")
        return None


def save_as_markdown(post: dict) -> str:
    """Markdown 파일로 저장하고 파일 경로 반환"""
    os.makedirs(POSTS_DIR, exist_ok=True)

    date_str = datetime.now().strftime("%Y-%m-%d")
    filename = f"{date_str}-{post['slug']}.md"
    filepath = os.path.join(POSTS_DIR, filename)

    # 슬러그가 중복이면 타임스탬프 추가
    if os.path.exists(filepath):
        ts = datetime.now().strftime("%H%M%S")
        filename = f"{date_str}-{post['slug']}-{ts}.md"
        filepath = os.path.join(POSTS_DIR, filename)

    frontmatter = f"""---
title: "{post['title']}"
date: "{date_str}"
category: "{post['category']}"
focusKeyword: "{post['focus_keyword']}"
metaDescription: "{post['meta_desc']}"
excerpt: "{post['meta_desc'][:120]}"
---

"""
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(frontmatter + post["body"])

    print(f"✅ Markdown 저장 완료: {filepath}")
    return filepath


def git_push(filepath: str, post_title: str):
    """변경사항을 git commit & push"""
    try:
        repo_path = GITHUB_REPO_PATH
        rel_path = os.path.relpath(filepath, repo_path)

        subprocess.run(["git", "-C", repo_path, "add", rel_path], check=True)
        commit_msg = f"✍️ 새 포스트: {post_title}"
        subprocess.run(["git", "-C", repo_path, "commit", "-m", commit_msg], check=True)
        subprocess.run(["git", "-C", repo_path, "push", "origin", "main"], check=True)

        print(f"✅ GitHub push 완료!")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Git push 오류: {e}")
        return False


def deploy_cloudflare():
    """Wrangler를 이용해 로컬에서 직접 Cloudflare Pages로 빌드 및 배포"""
    try:
        site_path = os.path.join(GITHUB_REPO_PATH, "site")
        print("⚙️ Next.js 정적 빌드 시작...")
        
        # Windows 환경 대응: npm.cmd, npx.cmd 사용
        npm_cmd = "npm.cmd" if os.name == "nt" else "npm"
        npx_cmd = "npx.cmd" if os.name == "nt" else "npx"

        # 1. 빌드
        subprocess.run([npm_cmd, "run", "build"], cwd=site_path, check=True)
        print("✅ 빌드 완료! Cloudflare Pages 배포 시작...")
        
        # 2. 배포
        deploy_cmd = [
            npx_cmd, "wrangler", "pages", "deploy", "out",
            "--project-name", "wellbeinghealth-site",
            "--commit-dirty=true"
        ]
        subprocess.run(deploy_cmd, cwd=site_path, check=True)
        print("🚀 Cloudflare Pages 배포 완료!")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Cloudflare 배포 오류: {e}")
        return False



def send_telegram(message: str):
    if not TELEGRAM_BOT_TOKEN or not TELEGRAM_CHAT_ID:
        return
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    try:
        requests.post(url, json={"chat_id": TELEGRAM_CHAT_ID, "text": message, "parse_mode": "HTML"})
        print("📲 텔레그램 알림 전송 완료!")
    except Exception as e:
        print(f"텔레그램 오류: {e}")


def post_job(time_of_day: str = "오전"):
    print(f"\n{'='*50}")
    print(f"🚀 {time_of_day} 포스팅 작업 시작 — {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"{'='*50}")

    topic = get_next_topic()

    if topic:
        print(f"📌 큐에서 주제: {topic['title']}")
        category = topic["category"]
        user_prompt = (
            f"오늘의 포스팅 주제는 '{topic['title']}'입니다. "
            f"소제목으로 {', '.join(topic['subtitles'])}을 반드시 포함하여 마크다운으로 작성해주세요. "
            f"카테고리는 '{category}'입니다."
        )
    else:
        print("🤖 큐 비어있음 — 자동 주제 선정")
        if time_of_day == "오전":
            category = random.choice(["운동", "다이어트", "건강식단"])
        else:
            category = random.choice(["생활습관", "멘탈케어"])
        user_prompt = (
            f"카테고리 '{category}'에 어울리는 흥미롭고 구체적인 주제를 하나 정해서 "
            f"블로그 포스팅을 마크다운 형식으로 작성해주세요."
        )

    post = generate_post(user_prompt)
    if not post:
        print("❌ 글 생성 실패")
        return

    filepath = save_as_markdown(post)
    pushed = git_push(filepath, post["title"])
    deployed = deploy_cloudflare()

    if pushed or deployed:
        msg = (
            f"🎉 <b>[웰빙헬스] 새 포스트 자동 발행!</b>\n\n"
            f"📝 <b>제목:</b> {post['title']}\n"
            f"🔑 <b>키워드:</b> {post['focus_keyword']}\n"
            f"🏷️ <b>카테고리:</b> {post['category']}\n"
            f"🌐 배포 상태: {'성공' if deployed else '실패'}"
        )
        send_telegram(msg)


if __name__ == "__main__":
    import schedule

    print("🚀 Wellbeing Health 정적 사이트 자동 포스팅 봇 시작!")
    print("스케줄: 오전 10시, 오후 3시")

    schedule.every().day.at("10:00").do(post_job, time_of_day="오전")
    schedule.every().day.at("15:00").do(post_job, time_of_day="오후")

    # 즉시 테스트하려면 주석 해제:
    # post_job("테스트")

    while True:
        schedule.run_pending()
        time.sleep(60)
