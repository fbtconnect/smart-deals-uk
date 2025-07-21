# Smart Deals UK

A Telegram-powered bot that scrapes Argos UK for bargains, filters them using a simple AI deal scorer, and alerts users.

## 🚀 Features
- Track UK products (Argos to start)
- Basic AI-powered deal filter
- Telegram bot alerts

## 🔧 Setup
1. Create a Telegram bot via @BotFather and get your API token.
2. Create a `.env` file in the root folder:
   ```
   TELEGRAM_BOT_TOKEN=your_token_here
   ```
3. Install dependencies: `pip install -r requirements.txt`
4. Run the bot from the root folder:
   ```bash
   python -m alert_system.telegram_bot
   ```

## 📌 Coming soon
- Amazon UK scraping
- Email alerts
- User preferences and watchlists
