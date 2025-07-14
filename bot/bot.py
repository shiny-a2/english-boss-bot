from bot.handlers import handle_message

async def process_telegram_update(update: dict):
    if 'message' in update:
        await handle_message(update['message'])
