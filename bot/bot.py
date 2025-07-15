import os
import aiohttp
import asyncio

BOT_TOKEN = os.getenv("BOT_TOKEN")
BASE_URL = f"https://api.telegram.org/bot{BOT_TOKEN}"

async def process_telegram_update(update: dict):
    print("✅ Update received:", update)  # 👈 این خیلی مهمه

    try:
        message = update.get("message", {})
        chat_id = message.get("chat", {}).get("id")
        text = message.get("text")

        print(f"📩 Message from {chat_id}: {text}")  # 👈 این هم مهمه

        if chat_id and text:
            await send_message(chat_id, f"تو نوشتی: {text}")
    except Exception as e:
        print("❌ Error while processing update:", e)

async def send_message(chat_id, text):
    url = f"{BASE_URL}/sendMessage"
    async with aiohttp.ClientSession() as session:
        async with session.post(url, json={"chat_id": chat_id, "text": text}) as resp:
            result = await resp.json()
            print("📤 Message sent:", result)  # 👈 پیام پاسخ
