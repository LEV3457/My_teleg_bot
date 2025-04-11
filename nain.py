
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext


KEYWORD_RESPONSES = {
    "привет": "Привет! Как дела? 😊",
    "как дела": "У меня всё отлично! А у тебя?",
    "пока": "До встречи! 👋",
    "бот": "Я здесь! Чем могу помочь?",
}


def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("Привет! Напиши мне что-нибудь, и я отвечу.")


def handle_message(update: Update, context: CallbackContext) -> None:
    user_message = update.message.text.lower()  
    for keyword, response in KEYWORD_RESPONSES.items():
        if keyword in user_message:
            update.message.reply_text(response)
            return

    update.message.reply_text("Я не понял вашего сообщения. Попробуйте ещё раз!")


def main() -> None:
    updater = Updater(TOKEN)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))

    updater.start_polling()
    print("Бот запущен и слушает сообщения...")
    updater.idle()


    # if __name__ == '__main__':  
    # asyncio.run(main())
