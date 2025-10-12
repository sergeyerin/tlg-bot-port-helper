# TLG Bot Portuguese Helper 🇵🇹

A Telegram bot that helps users learn Portuguese by providing verb conjugations and grammar corrections using OpenAI.

## Description

This bot provides two main features:
1. **Verb Conjugation**: Send any Portuguese verb in any form, and get all conjugations across different tenses
2. **Grammar Correction**: Send Portuguese phrases and get corrections with explanations

## Features

- 🔤 **Smart Text Analysis**: Automatically detects if input is a single verb or a phrase
- 📚 **Complete Verb Conjugations**: Shows all tenses including:
  - Present Indicative
  - Past Perfect (Pretérito Perfeito)
  - Imperfect (Pretérito Imperfeito)
  - Future (Futuro do Presente)
  - Conditional (Condicional)
  - Present Subjunctive (Presente do Subjuntivo)
  - Imperative (Imperativo)
- ✏️ **Grammar Correction**: Identifies and explains grammatical errors
- 🤖 **AI-Powered**: Uses OpenAI GPT models for accurate Portuguese language processing
- 📱 **Easy to Use**: Simple Telegram interface

## Installation

### Prerequisites

- Python 3.8 or higher
- Telegram Bot Token (get from [@BotFather](https://t.me/BotFather))
- OpenAI API Key (get from [OpenAI Platform](https://platform.openai.com/api-keys))

### Setup

1. **Clone the repository**
```bash
git clone https://github.com/sergeyerin/tlg-bot-port-helper.git
cd tlg-bot-port-helper
```

2. **Create virtual environment (recommended)**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Configure environment variables**
```bash
cp .env.example .env
```
Then edit `.env` file with your actual tokens:
```env
TELEGRAM_BOT_TOKEN=your_telegram_bot_token_here
OPENAI_API_KEY=your_openai_api_key_here
OPENAI_MODEL=gpt-3.5-turbo
BOT_DEBUG=false
```

## Usage

### Starting the Bot

```bash
python bot.py
```

### Bot Commands

- `/start` - Initialize the bot and see welcome message
- `/help` - Show help information

### Examples

**Verb Conjugation:**
- Send: `falar`
- Get: Complete conjugation table for the verb "falar"

**Grammar Correction:**
- Send: `Ontem eu foi ao mercado`
- Get: Corrected phrase with explanation

## Configuration

### Environment Variables

| Variable | Description | Required | Default |
|----------|-------------|----------|---------|
| `TELEGRAM_BOT_TOKEN` | Your Telegram bot token from @BotFather | ✅ Yes | - |
| `OPENAI_API_KEY` | Your OpenAI API key | ✅ Yes | - |
| `OPENAI_MODEL` | OpenAI model to use | ❌ No | `gpt-3.5-turbo` |
| `BOT_DEBUG` | Enable debug logging | ❌ No | `false` |

### Supported OpenAI Models

- `gpt-3.5-turbo` (recommended for cost-effectiveness)
- `gpt-4` (better accuracy, higher cost)
- `gpt-4-turbo-preview` (latest features)

## Project Structure

```
tlg-bot-port-helper/
├── bot.py              # Main bot application
├── config.py           # Configuration and environment setup
├── openai_helper.py    # OpenAI integration and language processing
├── requirements.txt    # Python dependencies
├── .env.example       # Environment variables template
├── .env               # Your actual environment variables (not in git)
├── .gitignore         # Git ignore rules
└── README.md          # This file
```

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.