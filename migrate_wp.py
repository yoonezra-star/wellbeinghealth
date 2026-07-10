"""
migrate_wp.py
=============
WordPress REST API에서 모든 포스트를 가져와
site/content/posts/ 에 Markdown 파일로 저장합니다.

사용법:
  python migrate_wp.py

.env 파일에 WP_URL, WP_USERNAME, WP_APP_PASSWORD 설정 필요.
"""

import os
import re
import json
import time
import requests
from datetime import datetime
from dotenv import load_dotenv
from requests.auth import HTTPBasicAuth

# HTML을 간단한 Markdown으로 변환 (html2text 없이)
try:
    import html2text
    HAS_HTML2TEXT = True
except ImportError:
    HAS_HTML2TEXT = False
    print("⚠️  html2text 미설치. pip install html2text 권장.")
    print("   일단 HTML 태그를 제거하고 저장합니다.\n")

load_dotenv()

WP_URL = os.getenv("WP_URL", "https://wellbeinghealth.co.kr")
WP_USERNAME = os.getenv("WP_USERNAME")
WP_APP_PASSWORD = os.getenv("WP_APP_PASSWORD")

POSTS_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "site", "content", "posts")

# WordPress 카테고리 ID → 이름 매핑
CATEGORY_MAP = {
    3: "운동",
    4: "다이어트",
    8: "건강식단",
    5: "생활습관",
    6: "멘탈케어",
    7: "전문가칼럼",
}


def html_to_markdown(html: str) -> str:
    if HAS_HTML2TEXT:
        h = html2text.HTML2Text()
        h.ignore_links = False
        h.body_width = 0
        return h.handle(html)
    else:
        # 간단한 태그 제거
        text = re.sub(r"<br\s*/?>", "\n", html, flags=re.IGNORECASE)
        text = re.sub(r"</p>", "\n\n", text, flags=re.IGNORECASE)
        text = re.sub(r"<h([1-6])[^>]*>(.*?)</h\1>", lambda m: "#" * int(m.group(1)) + " " + m.group(2) + "\n", text, flags=re.IGNORECASE | re.DOTALL)
        text = re.sub(r"<[^>]+>", "", text)
        text = re.sub(r"\n{3,}", "\n\n", text)
        return text.strip()


def slugify(text: str) -> str:
    """제목에서 URL 슬러그 생성"""
    # 한글은 제거하고 영문/숫자만 사용 (날짜로 대체)
    slug = re.sub(r"[^\w\s-]", "", text.lower())
    slug = re.sub(r"[\s_]+", "-", slug)
    slug = slug.strip("-")
    return slug if slug else "post"


def get_category_name(category_ids: list) -> str:
    for cat_id in category_ids:
        if cat_id in CATEGORY_MAP:
            return CATEGORY_MAP[cat_id]
    return "건강식단"


def get_all_posts():
    """WordPress REST API에서 모든 포스트 가져오기 (페이지네이션)"""
    posts = []
    page = 1
    auth = HTTPBasicAuth(WP_USERNAME, WP_APP_PASSWORD) if WP_USERNAME else None

    print(f"WordPress({WP_URL})에서 포스트 가져오는 중...")

    while True:
        url = f"{WP_URL}/wp-json/wp/v2/posts"
        params = {"page": page, "per_page": 100, "status": "publish"}

        try:
            resp = requests.get(url, params=params, auth=auth, timeout=30)
            if resp.status_code == 400:
                break  # 더 이상 페이지 없음
            resp.raise_for_status()
            batch = resp.json()
            if not batch:
                break
            posts.extend(batch)
            total_pages = int(resp.headers.get("X-WP-TotalPages", 1))
            print(f"  페이지 {page}/{total_pages} — {len(batch)}개 포스트")
            if page >= total_pages:
                break
            page += 1
            time.sleep(0.3)
        except Exception as e:
            print(f"API 오류 (페이지 {page}): {e}")
            break

    print(f"\n총 {len(posts)}개 포스트 가져옴.")
    return posts


def get_post_meta(post_id: int) -> dict:
    """포스트 메타데이터 (Rank Math SEO) 가져오기"""
    url = f"{WP_URL}/wp-json/wp/v2/posts/{post_id}"
    auth = HTTPBasicAuth(WP_USERNAME, WP_APP_PASSWORD) if WP_USERNAME else None
    try:
        resp = requests.get(url, auth=auth, timeout=15)
        data = resp.json()
        meta = data.get("meta", {}) or {}
        return {
            "focus_keyword": meta.get("rank_math_focus_keyword", ""),
            "meta_desc": meta.get("rank_math_description", ""),
        }
    except Exception:
        return {"focus_keyword": "", "meta_desc": ""}


def save_post(post: dict, index: int, total: int):
    """포스트를 Markdown 파일로 저장"""
    post_id = post["id"]
    title = post["title"]["rendered"]
    raw_html = post["content"]["rendered"]
    date_raw = post.get("date", "")[:10]  # YYYY-MM-DD
    category_ids = post.get("categories", [])

    category = get_category_name(category_ids)
    body_md = html_to_markdown(raw_html)

    # 슬러그: WordPress slug 사용
    wp_slug = post.get("slug", "")
    if not wp_slug:
        wp_slug = f"post-{post_id}"

    # 파일명: 날짜-슬러그.md
    filename = f"{date_raw}-{wp_slug}.md"
    filepath = os.path.join(POSTS_DIR, filename)

    # 메타 정보 (REST API 기본 응답에 포함된 경우)
    excerpt_raw = post.get("excerpt", {}).get("rendered", "")
    excerpt = re.sub(r"<[^>]+>", "", excerpt_raw).strip()[:200]

    frontmatter = f"""---
title: "{title.replace('"', "'")}"
date: "{date_raw}"
category: "{category}"
focusKeyword: ""
metaDescription: "{excerpt[:160].replace('"', "'")}"
excerpt: "{excerpt[:120].replace('"', "'")}"
wpId: {post_id}
---

"""

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(frontmatter + body_md)

    print(f"[{index+1:3d}/{total}] ✅ {filename}")
    return filepath


def main():
    os.makedirs(POSTS_DIR, exist_ok=True)

    posts = get_all_posts()
    if not posts:
        print("포스트가 없거나 API 연결에 실패했습니다.")
        return

    print(f"\n총 {len(posts)}개 포스트를 Markdown으로 변환합니다...\n")

    success = 0
    for i, post in enumerate(posts):
        try:
            save_post(post, i, len(posts))
            success += 1
            time.sleep(0.1)
        except Exception as e:
            print(f"  ❌ 변환 실패 (ID: {post.get('id')}): {e}")

    print(f"\n{'='*50}")
    print(f"✅ 완료! {success}/{len(posts)}개 포스트 변환 성공")
    print(f"저장 위치: {POSTS_DIR}")
    print(f"{'='*50}")


if __name__ == "__main__":
    main()
