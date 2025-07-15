import os
import httpx
from bot.messages import WELCOME, QUESTIONS
from backend.openai_api import get_openai_level

BOT_TOKEN = os.getenv("BOT_TOKEN")
API_URL = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

user_sessions = {}

async def send_message(chat_id: int, text: str):
    async with httpx.AsyncClient() as client:
        await client.post(API_URL, json={"chat_id": chat_id, "text": text})

async def process_telegram_update(update: dict):
    message = update.get("message")
    if not message:
        return

    chat_id = message["chat"]["id"]
    text = message.get("text", "").strip()

    if text == "/start":
        user_sessions[chat_id] = {"step": 0, "answers": []}
        await send_message(chat_id, WELCOME + f"\n\n1️⃣ {QUESTIONS[0]}")
        return

    session = user_sessions.get(chat_id)
    if not session:
        await send_message(chat_id, "برای شروع دستور /start را وارد کن.")
        return

    session["answers"].append(text)
    session["step"] += 1

    if session["step"] < len(QUESTIONS):
        await send_message(chat_id, f"{session['step']+1}️⃣ {QUESTIONS[session['step']]}")
    else:
        level = await get_openai_level(session["answers"])
        del user_sessions[chat_id]
        await send_message(chat_id, f"🔍 سطح زبانت به نظر می‌رسه: *{level}*")
