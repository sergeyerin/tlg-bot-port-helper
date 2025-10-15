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
🇵🇹 Привет! Добро пожаловать в помощник европейского португальского языка! 🇷🇺

Я специализируюсь на **европейском португальском** и могу помочь:

1️⃣ **Спряжение глаголов**: Отправьте португальский глагол, и я покажу все спряжения в европейском стандарте.
   Пример: "falar", "falou", "falarei"

2️⃣ **Исправление фраз (особое внимание предлогам)**: Отправьте фразу, и я тщательно проверю предлоги и грамматику.
   Пример: "Vou ao mercado para comprar pão"

🇦🇻 **Особенности**: Использую только европейские нормы и орфографию!

Напишите /help чтобы увидеть это сообщение снова.
"""

HELP_MESSAGE = """
🆘 **Как использовать бота европейского португальского:**

📝 **Для спряжения глаголов:**
- Напишите любую форму португальского глагола
- Получите все спряжения в европейском стандарте
- Пример: "correr", "corri", "correria"

📝 **Для исправления фраз (ПРЕДЛОГИ - моя специальность!):**
- Напишите полную фразу на португальском
- Особое внимание предлогам (de, em, por, para, a, com, etc.)
- Пример: "Vou para o mercado" или "Estou a estudar"

🇦🇻 **Особенности европейского португальского:**
- Закрытые гласные (ê, ô)
- Формы "tu" и "vós"
- Специальные правила использования предлогов

🔧 **Команды:**
/start - Запустить бота • /help - Показать справку

Отправьте текст - и я автоматически определю, нужно ли спрягать глагол или исправить фразу!
"""
