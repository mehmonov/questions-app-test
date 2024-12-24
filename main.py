import logging
import sys
from os import getenv
from aiogram import Bot, Dispatcher, F
from aiogram.client.default import DefaultBotProperties
from aiogram.enums.parse_mode import ParseMode
from aiogram.types import Message, KeyboardButton, ReplyKeyboardMarkup, WebAppInfo
from aiogram.filters import Command

TOKEN = "7675290255:AAGSd00ocIHM0-bA8cZkVdeIMTqaR3GvePo"
APP_BASE_URL = "https://questions-app-test.vercel.app"

async def start_handler(message: Message):
    web_app = WebAppInfo(url=APP_BASE_URL)
    
    await message.answer(
        "Web ilovani ochish uchun pastdagi tugmani bosing.",
        reply_markup=ReplyKeyboardMarkup(
            keyboard=[
                [KeyboardButton(text="Web App", web_app=web_app)]
            ],
            resize_keyboard=True
        )
    )

async def main():
    bot = Bot(
        token=TOKEN, 
        default=DefaultBotProperties(parse_mode=ParseMode.HTML)
    )
    
    dp = Dispatcher()
    dp["base_url"] = APP_BASE_URL
    
    dp.message.register(start_handler, Command("start"))
    
    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    try:
        import asyncio
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logging.info("Bot stopped!")
