import os
import logging
from aiogram import Bot, Dispatcher, types
from aiogram import F
from aiohttp import web

# Loggingni sozlash
logging.basicConfig(level=logging.INFO)

# Bot tokenini muhit o'zgaruvchisidan olish
API_TOKEN = os.getenv('7777111228:AAFJNsgzYXjfd1fNXIbffB8IhNBnwC5Nj6g')

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
