import os
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from telegram import Update

TOKEN = os.getenv("TELEGRAM_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Meme Alpha Bot is running 🚀")

async def alpha(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Scanning wallets... potential meme coin coming soon 👀")

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("alpha", alpha))

print("Bot is running...")

app.run_polling()
