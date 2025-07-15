from fastapi import FastAPI, Request
from backend.openai_api import get_openai_level
from bot.bot import process_telegram_update

app = FastAPI()

@app.get("/")
def home():
    return {"status": "English Boss is running"}

@app.post("/webhook")
async def telegram_webhook(request: Request):
    update = await request.json()
    await process_telegram_update(update)
    return {"ok": True}
