import os
from fastapi import FastAPI, Request
from openai_api import get_openai_level
from bot.bot import process_telegram_update
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

app = FastAPI()

@app.get("/")
def home():
    return {"status": "English Boss is running"}

@app.post("/webhook")
async def telegram_webhook(request: Request):
    update = await request.json()
    await process_telegram_update(update)
    return {"ok": True}

if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run("backend.main:app", host="0.0.0.0", port=port)