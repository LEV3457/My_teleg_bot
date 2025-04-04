import asyncio
import os
from loguru import logger
from aiogram import Bot, Dispatcher, types, F, Router
from aiogram.filters import Command
from dotenv import find_dotenv, load_dotenv
from aiogram.enums import ChatType


router = Router()


load_dotenv(find_dotenv())
TOKEN = os.getenv("TOKEN")


async def main():
    logger.add("file.log",
            format="{time:YYYY-MM-DD at HH:mm:ss} | {level} | {message}",
            rotation="3 days",
            backtrace=True,
            diagnose=True)

    bot = Bot(TOKEN)
    logger.info("Бот создан")
    dp = Dispatcher()
    logger.info("Диспетчер создан")

    @dp.message(Command("start"))
    async def send_welcome(message: types.Message):
        await message.answer("Привет, Я собутыльник на час!")
        await message.answer("что нужно: /start и /help")
        logger.info("Бот ответил на команду /start")


    @dp.message(Command("help"))
    async def help(message: types.Message):
        await message.answer("держи подарочек")
        logger.info("Бот обьяснил, что делает")

    # @dp.message()
    # async def echo(message: types.Message):
    #     await message.answer(message.text)
    #     logger.info(f"Бот вернул пользователю сообщение {message.text}")

    await dp.start_polling(bot)


    @router.message(
        F.chat.type.in_([ChatType.GROUP, ChatType.SUPERGROUP]),
        F.text.lower().contains('дать')
        )
    async def cry(message: types.Message):
        sender = message.from_user
        sender_username = f"@{sender.username}" if sender.username else sender.first_name
        await message.reply(f"{sender_username} нет конфет")


    @router.message(
        F.chat.type.in_([ChatType.GROUP, ChatType.SUPERGROUP]),
        F.text.lower().contains("люблю")
    )
    async def interactive_love(message: types.Message):
        await message.reply("А я вас нет")


    @router.message(
        F.chat.type.in_([ChatType.GROUP, ChatType.SUPERGROUP]),
        F.text.lower().contains('дать')
)
    async def cry(message: types.Message):
        sender = message.from_user
        sender_username = f"@{sender.username}" if sender.username else sender.first_name
        await message.reply(f"{sender_username} нет конфет")
    
    

    @router.message(
        F.chat.type.in_([ChatType.GROUP, ChatType.SUPERGROUP]),
        F.text.lower().contains("радоваться")
    )
    async def interactive_love(message: types.Message):
        await message.reply(" ты радуешься")
    


if __name__ == '__main__':
    asyncio.run(main())
