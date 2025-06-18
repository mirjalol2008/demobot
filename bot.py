import os
import logging
from aiogram import Bot, Dispatcher, types, F
from aiogram.enums import ParseMode
from aiogram.types import Message
from aiogram.filters import Command

from dotenv import load_dotenv
import asyncio

# Muhit o'zgaruvchilarini yuklash
load_dotenv()

# Loggingni sozlash
logging.basicConfig(level=logging.INFO)

# Bot tokenini olish
API_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')

if API_TOKEN is None:
    raise ValueError("TELEGRAM_BOT_TOKEN muhit o'zgaruvchisi topilmadi.")

# Bot va Dispatcher obyektlari
bot = Bot(token=API_TOKEN, parse_mode=ParseMode.HTML)
dp = Dispatcher()

# /start komandasi
@dp.message(Command("start"))
async def start_handler(message: Message):
    await message.answer("👋 Salom! Bu mening Telegram botim.")

# Echo handler
@dp.message()
async def echo_handler(message: Message):
    await message.answer(message.text)

# Botni ishga tushirish
async def main():
    logging.info("Bot ishga tushmoqda...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
