import os
import requests
from telegram import Bot
from telegram.ext import ApplicationBuilder, CommandHandler

TOKEN = os.getenv("TELEGRAM_TOKEN")

bot = Bot(token=TOKEN)

async def start(update, context):
    await update.message.reply_text("Meme Alpha Bot is running 🚀")

async def alpha(update, context):
    await update.message.reply_text("Scanning wallets... potential meme coin coming soon 👀")

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("alpha", alpha))

app.run_polling()