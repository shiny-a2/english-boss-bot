import os
import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import openai
from apscheduler.schedulers.background import BackgroundScheduler
from services.openai_api import ask_openai

# تنظیمات لاگ
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
logger = logging.getLogger(__name__)

# خواندن کلیدها از متغیر محیطی
BOT_TOKEN = os.getenv("BOT_TOKEN")
OPENAI_KEY = os.getenv("OPENAI_KEY")

if not BOT_TOKEN or not OPENAI_KEY:
    logger.error("Error: BOT_TOKEN or OPENAI_KEY environment variables not set.")
    exit(1)

openai.api_key = OPENAI_KEY

def start(update, context):
    update.message.reply_text(
        "سلام! من English Boss هستم. با من می‌تونی انگلیسی‌ات رو تقویت کنی. سوالی داری بپرس!"
    )

def help_command(update, context):
    update.message.reply_text("دستورهای موجود:\n/start\n/help")

def handle_message(update, context):
    user_text = update.message.text
    try:
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=user_text,
            max_tokens=150,
            n=1,
            stop=None,
            temperature=0.7,
        )
        answer = response.choices[0].text.strip()
    except Exception as e:
        logger.error(f"OpenAI API error: {e}")
        answer = "متاسفانه مشکلی پیش آمد. لطفا دوباره تلاش کنید."

    update.message.reply_text(answer)

def handle_text(update, context):
    user_message = update.message.text
    reply = ask_openai(user_message)
    update.message.reply_text(reply)

def error(update, context):
    logger.warning(f'Update {update} caused error {context.error}')

def main():
    updater = Updater(BOT_TOKEN, use_context=True)
    dp = updater.dispatcher

    # اضافه کردن همه هندلرها
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help_command))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_text))

    dp.add_error_handler(error)

    # اجرای بات
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
import os
import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import openai
from apscheduler.schedulers.background import BackgroundScheduler
from services.openai_api import ask_openai

# تنظیمات لاگ
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
logger = logging.getLogger(__name__)

# خواندن کلیدها از متغیر محیطی
BOT_TOKEN = os.getenv("BOT_TOKEN")
OPENAI_KEY = os.getenv("OPENAI_KEY")

if not BOT_TOKEN or not OPENAI_KEY:
    logger.error("Error: BOT_TOKEN or OPENAI_KEY environment variables not set.")
    exit(1)

openai.api_key = OPENAI_KEY

def start(update, context):
    update.message.reply_text(
        "سلام! من English Boss هستم. با من می‌تونی انگلیسی‌ات رو تقویت کنی. سوالی داری بپرس!"
    )

def help_command(update, context):
    update.message.reply_text("دستورهای موجود:\n/start\n/help")

def handle_message(update, context):
    user_text = update.message.text
    try:
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=user_text,
            max_tokens=150,
            n=1,
            stop=None,
            temperature=0.7,
        )
        answer = response.choices[0].text.strip()
    except Exception as e:
        logger.error(f"OpenAI API error: {e}")
        answer = "متاسفانه مشکلی پیش آمد. لطفا دوباره تلاش کنید."

    update.message.reply_text(answer)

def handle_text(update, context):
    user_message = update.message.text
    reply = ask_openai(user_message)
    update.message.reply_text(reply)

def error(update, context):
    logger.warning(f'Update {update} caused error {context.error}')

def main():
    updater = Updater(BOT_TOKEN, use_context=True)
    dp = updater.dispatcher

    # اضافه کردن همه هندلرها
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help_command))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_text))

    dp.add_error_handler(error)

    # اجرای بات
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
