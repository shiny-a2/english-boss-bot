from fastapi import FastAPI, Request
from contextlib import asynccontextmanager
from bot.bot import process_telegram_update

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("🚀 English Boss Bot is up and running on /webhook")
    yield
    print("🛑 Shutting down...")

app = FastAPI(lifespan=lifespan)

@app.get("/")
def home():
    return {"status": "✅ English Boss is running"}

@app.post("/webhook")
async def telegram_webhook(request: Request):
    try:
        update = await request.json()
        print("✅ Update received:", update)
        await process_telegram_update(update)
        return {"ok": True}
    except Exception as e:
        print("❌ Error in /webhook:", e)
        return {"ok": False, "error": str(e)}
