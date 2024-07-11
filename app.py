from flask import Flask, request
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from config import TELEGRAM_BOT_TOKEN

app = Flask(__name__)

# Initialize the bot application
bot_app = ApplicationBuilder().token(TELEGRAM_BOT_TOKEN).build()

# Define the start command handler
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user = update.effective_user
    await update.message.reply_text(
        f'Hello {user.first_name}, welcome to SpaceDrift! 🚀 Embark on an epic journey across the cosmos in this exciting blockchain game on the Ton network. Explore distant galaxies, complete thrilling missions, and earn valuable token rewards as you progress. Join our vibrant community of space adventurers and start your interstellar adventure today. Happy exploring! 🌌'
    )

# Register the /start command handler
bot_app.add_handler(CommandHandler("start", start))

# Define a route to handle incoming updates from Telegram
@app.route('/webhook', methods=['POST'])
async def webhook():
    # Retrieve the message in JSON format
    update = Update.de_json(request.get_json(force=True), bot_app.bot)
    # Process the update with the bot application
    await bot_app.process_update(update)
    return 'ok'

if __name__ == '__main__':
    # Set the webhook (this should be done once)
    bot_app.bot.set_webhook('https://<your-domain>/webhook')
    # Run the Flask app
    app.run(port=5000)