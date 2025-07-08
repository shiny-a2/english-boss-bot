import os
import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import openai

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

BOT_TOKEN = os.getenv("BOT_TOKEN")
OPENAI_KEY = os.getenv("OPENAI_KEY")

if not BOT_TOKEN or not OPENAI_KEY:
    logger.error("Error: BOT_TOKEN or OPENAI_KEY environment variables not set.")
    exit(1)

openai.api_key = OPENAI_KEY

def start(update, context):
    update.message.reply_text("سلام! من English Boss هستم. سوالت رو بپرس.")

def handle_text(update, context):
    user_message = update.message.text
    try:
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=user_message,
            max_tokens=150,
            temperature=0.7,
        )
        reply = response.choices[0].text.strip()
    except Exception as e:
        logger.error(f"OpenAI API error: {e}")
        reply = "متاسفانه مشکلی پیش آمد. لطفا دوباره تلاش کنید."
    update.message.reply_text(reply)

def main():
    updater = Updater(BOT_TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_text))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
