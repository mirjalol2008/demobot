import os
import logging
from aiogram import Bot, types, F
from aiogram import Dispatcher
from aiohttp import web

# Loggingni sozlash
logging.basicConfig(level=logging.INFO)

# Bot tokenini muhit o'zgaruvchisidan olish
API_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')

# Tokenni tekshirish
if API_TOKEN is None:
    raise ValueError("TELEGRAM_BOT_TOKEN muhit o'zgaruvchisi topilmadi. Iltimos, to'g'ri tokenni belgilang.")

# Bot va Dispatcher yaratish
bot = Bot(token=API_TOKEN)
dp = Dispatcher()

# /start komandasi uchun handler
@dp.message(F.command("start"))
async def send_welcome(message: types.Message):
    await message.reply("Salom! Bu mening Telegram botim.")

# Har qanday xabarni qaytarish uchun handler
@dp.message()
async def echo_message(message: types.Message):
    await message.answer(message.text)

# Web server ishga tushishi uchun qo'shimcha route
async def hello(request):
    return web.Response(text="Bot online!")

# Web application uchun routni qo'shish
app = web.Application()
app.router.add_get('/', hello)

# Botni ishga tushirish
async def main():
    await bot.delete_webhook()  # Oldin o'rnatilgan webhookni o'chirish
    await dp.start_polling(bot)

# Web serverni ishga tushirish
if __name__ == '__main__':
    logging.info("Bot ishga tushmoqda...")
    web.run_app(app, port=int(os.environ.get("PORT", 10000)))
