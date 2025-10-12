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
🇵🇹 Olá! Bem-vindo ao assistente de português! 🇵🇹

Eu posso ajudá-lo de duas formas:

1️⃣ **Conjugação de verbos**: Envie um verbo português em qualquer forma e eu mostrarei todas as conjugações.
   Exemplo: "falar" ou "falou" ou "falarei"

2️⃣ **Correção de frases**: Envie uma frase em português e eu a corrigirei se houver erros.
   Exemplo: "Eu gosto muito de comer pizza"

Digite /help para ver esta mensagem novamente.
"""

HELP_MESSAGE = """
🆘 **Como usar o bot:**

📝 **Para conjugar verbos:**
- Digite qualquer forma de um verbo português
- Exemplo: "correr", "corri", "correria"

📝 **Para corrigir frases:**
- Digite uma frase completa em português
- Exemplo: "Ontem eu foi ao mercado"

🔧 **Comandos disponíveis:**
/start - Iniciar o bot
/help - Mostrar esta ajuda

Envie qualquer texto e eu tentarei identificar se é um verbo para conjugar ou uma frase para corrigir!
"""