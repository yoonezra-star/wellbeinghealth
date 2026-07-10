import random
import time
from auto_poster import generate_post, post_to_wordpress, CATEGORIES

backfill_schedule = [
    {"date": "2026-04-28T10:00:00", "type": "morning"},
    {"date": "2026-04-28T15:00:00", "type": "afternoon"},
    {"date": "2026-04-29T10:00:00", "type": "morning"},
    {"date": "2026-04-29T15:00:00", "type": "afternoon"},
    {"date": "2026-04-30T10:00:00", "type": "morning"},
    {"date": "2026-04-30T15:00:00", "type": "afternoon"},
    {"date": "2026-05-01T10:00:00", "type": "morning"},
    {"date": "2026-05-01T15:00:00", "type": "afternoon"}
]

morning_cats = ["운동", "다이어트", "건강식단"]
afternoon_cats = ["생활습관", "멘탈케어"]

print("🚀 과거 날짜(4월 28일 ~ 5월 1일) 백필(Backfill) 발행을 시작합니다! 총 8개 포스팅 생성...")

for item in backfill_schedule:
    post_date = item["date"]
    post_type = item["type"]
    
    if post_type == "morning":
        chosen_cat = random.choice(morning_cats)
    else:
        chosen_cat = random.choice(afternoon_cats)
        
    cat_id = CATEGORIES[chosen_cat]
    
    print(f"\n[{post_date}] '{chosen_cat}' 카테고리 글 생성 중...")
    
    title, body, focus_keyword, meta_desc = generate_post(chosen_cat)
    
    if title and body:
        post_to_wordpress(title, body, focus_keyword, meta_desc, cat_id, post_date=post_date)
        print(f"✅ {post_date} 발행 완료: {title}")
    else:
        print(f"❌ {post_date} 발행 실패 (글 생성 오류)")
        
    # 과도한 API 호출 방지 및 자연스러운 발행을 위해 대기
    time.sleep(10)

print("\n🎉 모든 백필 작업이 완료되었습니다!")
