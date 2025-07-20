from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from scraper.argos_scraper import get_argos_deals

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Welcome to SmartDeals UK! Send /track <item> to search Argos.")

async def track(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = ' '.join(context.args)
    deals = get_argos_deals(query)
    if not deals:
        await update.message.reply_text("No deals found.")
    else:
        reply = "\n".join([f"{d['title']} – {d['price']}" for d in deals[:5]])
        await update.message.reply_text(reply)

def run_bot():
    app = ApplicationBuilder().token("YOUR_TELEGRAM_BOT_TOKEN").build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("track", track))
    app.run_polling()
