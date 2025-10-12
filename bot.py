"""Main Telegram bot file for Portuguese Helper Bot."""

import asyncio
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from telegram.constants import ParseMode

from config import TELEGRAM_BOT_TOKEN, WELCOME_MESSAGE, HELP_MESSAGE, logger
from openai_helper import process_text

class PortugueseHelperBot:
    """Portuguese Helper Telegram Bot."""
    
    def __init__(self):
        """Initialize the bot."""
        self.application = Application.builder().token(TELEGRAM_BOT_TOKEN).build()
        self._setup_handlers()
    
    def _setup_handlers(self):
        """Setup bot command and message handlers."""
        # Command handlers
        self.application.add_handler(CommandHandler("start", self.start_command))
        self.application.add_handler(CommandHandler("help", self.help_command))
        
        # Message handlers
        self.application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, self.handle_message))
        
        # Error handler
        self.application.add_error_handler(self.error_handler)
    
    async def start_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Handle /start command."""
        user = update.effective_user
        logger.info(f"User {user.id} ({user.username}) started the bot")
        
        await update.message.reply_text(
            WELCOME_MESSAGE,
            parse_mode=ParseMode.MARKDOWN
        )
    
    async def help_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Handle /help command."""
        await update.message.reply_text(
            HELP_MESSAGE,
            parse_mode=ParseMode.MARKDOWN
        )
    
    async def handle_message(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Handle text messages from users."""
        user = update.effective_user
        user_text = update.message.text
        
        logger.info(f"User {user.id} ({user.username}) sent: {user_text}")
        
        # Send typing indicator
        await context.bot.send_chat_action(chat_id=update.effective_chat.id, action='typing')
        
        try:
            # Process the text with OpenAI
            response = await process_text(user_text)
            
            # Send the response
            await update.message.reply_text(
                response,
                parse_mode=ParseMode.MARKDOWN
            )
            
            logger.info(f"Sent response to user {user.id}")
            
        except Exception as e:
            logger.error(f"Error processing message from user {user.id}: {e}")
            await update.message.reply_text(
                "❌ Извините, произошла ошибка при обработке вашего сообщения. Попробуйте снова позже.",
                parse_mode=ParseMode.MARKDOWN
            )
    
    async def error_handler(self, update: object, context: ContextTypes.DEFAULT_TYPE):
        """Handle errors."""
        logger.error(f"Exception while handling an update: {context.error}")
    
    def run(self):
        """Start the bot."""
        logger.info("Starting Portuguese Helper Bot...")
        self.application.run_polling(allowed_updates=Update.ALL_TYPES)

def main():
    """Main function to run the bot."""
    try:
        bot = PortugueseHelperBot()
        bot.run()
    except KeyboardInterrupt:
        logger.info("Bot stopped by user")
    except Exception as e:
        logger.error(f"Error starting bot: {e}")
        raise

if __name__ == "__main__":
    main()