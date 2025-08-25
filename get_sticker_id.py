from telegram import Update
from telegram.ext import Application, MessageHandler, filters, ContextTypes

BOT_TOKEN = "8278841870:AAFG2D9dBcU6QXR6lctmnfeNRvJnrzXh-WA"  # paste your token from BotFather here

async def get_file_id(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.sticker:
        sticker = update.message.sticker
        # Print the file_id in the terminal
        print(f"Sticker File ID: {sticker.file_id}")
        # Also reply in chat so you can see it in Telegram
        await update.message.reply_text(f"Sticker ID: {sticker.file_id}")

# Build the bot
app = Application.builder().token(BOT_TOKEN).build()
app.add_handler(MessageHandler(filters.Sticker.ALL, get_file_id))

print("Send your sticker to the bot now...")
app.run_polling()
