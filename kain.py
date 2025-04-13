from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes


TOKEN = " s "


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Привет! Я ")


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_text = update.message.text.lower() 
    
    if user_text == "привет":
        await update.message.reply_text("Пупик")
    elif user_text == "погода":
        await update.message.reply_text("выйди на удицу")
    elif user_text == "радоваться":
        await update.message.reply_text("чо радуешься")
    else:
        await update.message.reply_text("Я не понимаю. Иди поработай")


if __name__ == "__main__":
    print("Запускаю бота...")
    
    
    app = Application.builder().token(TOKEN).build()

    
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    
    
    app.run_polling()