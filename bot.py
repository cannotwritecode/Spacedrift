from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from config import TELEGRAM_BOT_TOKEN

updater = Updater(TELEGRAM_BOT_TOKEN, use_context=True)
# Your bot logic here
# My bot token from BotFather

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /start is issued."""
    user = update.effective_user
    await update.message.reply_text(f'Hello {user.first_name}, welcome to SpaceDrift! 🚀 Embark on an epic journey across the cosmos in this exciting blockchain game on the Ton network. Explore distant galaxies, complete thrilling missions, and earn valuable token rewards as you progress. Join our vibrant community of space adventurers and start your interstellar adventure today. Happy exploring! 🌌')

def main() -> None:
    """Start the bot."""
    # Create the Application and pass it your bot's token
    application = ApplicationBuilder().token(TELEGRAM_BOT_TOKEN,).build()

    # Register the /start command handler
    application.add_handler(CommandHandler("start", start))

    # Start the Bot
    application.run_polling()

if __name__ == '__main__':
    main()