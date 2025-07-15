import os
import httpx
from bot.messages import WELCOME, QUESTIONS
from backend.openai_api import get_openai_level

# گرفتن توکن از متغیر محیطی
BOT_TOKEN = os.getenv("BOT_TOKEN")
API_URL = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

# ذخیره‌ی وضعیت کاربرها در حافظه
user_sessions = {}

# تابع برای ارسال پیام به کاربر
async def send_message(chat_id: int, text: str):
    async with httpx.AsyncClient() as client:
        await client.post(API_URL, json={"chat_id": chat_id, "text": text})

# هندل اصلی پیام‌ها
async def handle_message(message: dict):
    chat_id = message["chat"]["id"]
    text = message.get("text", "").strip()

    # شروع چت با /start
    if text.lower() == "/start":
        user_sessions[chat_id] = {"step": 0, "answers": []}
        await send_message(chat_id, WELCOME + f"\n\n1️⃣ {QUESTIONS[0]}")
        return

    # اگر کاربر بدون /start پیام داد
    session = user_sessions.get(chat_id)
    if not session:
        await send_message(chat_id, "لطفاً ابتدا /start رو بزن تا شروع کنیم 😊")
        return

    # ذخیره‌ی پاسخ کاربر
    session["answers"].append(text)
    session["step"] += 1

    # اگر هنوز سوالات باقی مونده
    if session["step"] < len(QUESTIONS):
        await send_message(chat_id, f"{session['step'] + 1}️⃣ {QUESTIONS[session['step']]}")
    else:
        # تحلیل سطح با OpenAI
        level = await get_openai_level(session["answers"])
        del user_sessions[chat_id]
        await send_message(chat_id, f"🎯 سطح تقریبی زبانت: {level}\n\n✅ الان می‌تونیم تمرین‌هاتو با توجه به سطحت شروع کنیم.")
