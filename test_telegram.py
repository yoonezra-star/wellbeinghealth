import os
from dotenv import load_dotenv
import requests

load_dotenv()

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

def send_telegram_message(message):
    if not TELEGRAM_BOT_TOKEN or not TELEGRAM_CHAT_ID:
        print("⚠️ 텔레그램 설정이 되어있지 않아 알림을 건너뜁니다.")
        return
        
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": message,
        "parse_mode": "HTML"
    }
    try:
        response = requests.post(url, json=payload)
        if response.status_code == 200:
            print("Telegram notification sent successfully!")
        else:
            print(f"Telegram send failed: {response.status_code} - {response.text}")
    except Exception as e:
        print(f"Telegram error: {e}")

if __name__ == "__main__":
    test_msg = "🎉 <b>새로운 포스팅이 자동 발행되었습니다!</b>\n\n📝 <b>제목:</b> 요가로 시작하는 마음과 몸의 균형 찾기\n🔑 <b>키워드:</b> 요가\n🔗 <b>주소:</b> https://wellbeinghealth.co.kr/요가로-시작하는-마음과-몸의-균형-찾기/"
    send_telegram_message(test_msg)
