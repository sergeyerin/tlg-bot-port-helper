"""Configuration module for the Portuguese Helper Bot."""

import os
import logging
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Telegram Bot Configuration
TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
if not TELEGRAM_BOT_TOKEN:
    raise ValueError("TELEGRAM_BOT_TOKEN environment variable is required")

# OpenAI Configuration
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
if not OPENAI_API_KEY:
    raise ValueError("OPENAI_API_KEY environment variable is required")

OPENAI_MODEL = os.getenv('OPENAI_MODEL', 'gpt-3.5-turbo')

# Bot Configuration
BOT_DEBUG = os.getenv('BOT_DEBUG', 'false').lower() == 'true'

# Logging Configuration
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.DEBUG if BOT_DEBUG else logging.INFO
)

logger = logging.getLogger(__name__)

# Bot Messages
WELCOME_MESSAGE = """
🇵🇹 Привет! Добро пожаловать в помощник португальского языка! 🇷🇺

Я могу помочь вам двумя способами:

1️⃣ **Спряжение глаголов**: Отправьте португальский глагол в любой форме, и я покажу все спряжения.
   Пример: "falar" или "falou" или "falarei"

2️⃣ **Исправление фраз**: Отправьте фразу на португальском языке, и я исправлю ошибки с объяснениями.
   Пример: "Eu gosto muito de comer pizza"

Напишите /help чтобы увидеть это сообщение снова.
"""

HELP_MESSAGE = """
🆘 **Как использовать бота:**

📝 **Для спряжения глаголов:**
- Напишите любую форму португальского глагола
- Пример: "correr", "corri", "correria"

📝 **Для исправления фраз:**
- Напишите полную фразу на португальском языке
- Пример: "Ontem eu foi ao mercado"

🔧 **Доступные команды:**
/start - Запустить бота
/help - Показать эту справку

Отправьте любой текст, и я попробую определить, это глагол для спряжения или фраза для исправления!
"""
