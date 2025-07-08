from telegram.ext import Updater, CommandHandler
from config import BOT_TOKEN
from daily import today_command
from chat import chat_command
from reminder import schedule_reminders
import os

BOT_TOKEN = os.getenv("BOT_TOKEN")
OPENAI_KEY = os.getenv("OPENAI_KEY")


def start(update, context):
    update.message.reply_text("👋 Welcome to *English Boss by AmirAli*!\nType /today to get your daily training.", parse_mode="Markdown")

updater = Updater(BOT_TOKEN)
dp = updater.dispatcher

dp.add_handler(CommandHandler("start", start))
dp.add_handler(CommandHandler("today", today_command))
dp.add_handler(CommandHandler("chat", chat_command))

schedule_reminders(updater.job_queue)

updater.start_polling()
updater.idle()
