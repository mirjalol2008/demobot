import os
import logging
from aiogram import Bot, types
from aiogram import F
from aiogram import Application
from aiohttp import web

# Loggingni sozlash
logging.basicConfig(level=logging.INFO)

# Bot tokenini muhit o'zgaruvchisidan olish
API_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')

# Tokenni tekshirish
if API_TOKEN is None:
    raise ValueError("TELEGRAM_BOT_TOKEN muhit o'zgaruvchisi topilmadi. Iltimos, to'g'ri tokenni belgilang.")

# Bot va Application yaratish
bot = Bot(token=API_TOKEN)
app = Application()

# /start komandasi uchun handler
@app.message(F.command("start"))
async def send_welcome(message: types.Message):
    await message.reply("Salom! Bu mening Telegram botim.")

# Har qanday xabarni qaytarish uchun handler
@app.message()
async def echo_message(message: types.Message):
    await message.answer(message.text)

# Web server ishga tushishi uchun qo'shimcha route
async def hello(request):
    return web.Response(text="Bot online!")

# Web application uchun routni qo'shish
app.router.add_get('/', hello)

# Web serverni ishga tushirish
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 10000))
    logging.info(f"Bot ishga tushdi: {port} portda")
    web.run_app(app, port=port)
