import os
import logging
from aiogram import Bot, Dispatcher, types
from aiogram import F
from aiohttp import web
from dotenv import load_dotenv

# .env faylini yuklash (agar siz foydalanayotgan bo'lsangiz)
load_dotenv()

# Loggingni sozlash
logging.basicConfig(level=logging.INFO)

# Bot tokenini muhit o'zgaruvchisidan olish
API_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')

# Tokenni tekshirish
if API_TOKEN is None:
    raise ValueError("TELEGRAM_BOT_TOKEN muhit o'zgaruvchisi topilmadi. Iltimos, to'g'ri tokenni belgilang.")

# Bot va dispatcher yaratish
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

# /start komandasi uchun handler
@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Salom! Bu mening Telegram botim.")

# Har qanday xabarni qaytarish uchun handler
@dp.message_handler()
async def echo_message(message: types.Message):
    await message.answer(message.text)

# Web server va Telegram botini ishga tushirish
if __name__ == '__main__':
    app = web.Application()
    
    # Samarali javoblar uchun routelar qo'shish
    async def hello(request):
        return web.Response(text="Bot online!")

    app.router.add_get('/', hello)

    # Web app ishga tushadigan port
    port = int(os.environ.get("PORT", 10000))
    web.run_app(app, port=port)
