import logging
import os
from aiogram import Bot, Dispatcher, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils import executor
from aiogram.dispatcher.storage.memory import MemoryStorage
from dotenv import load_dotenv

# .env fayldan TOKEN olish
load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")
ADMIN_ID = os.getenv("ADMIN_ID")  # Admin ID-ni .env faylda saqlaymiz

# Bot va Dispatcher yaratish
bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())

# Boshlang'ich tugmalar
def main_menu():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(KeyboardButton("📤 Maqola joylash"))
    keyboard.add(KeyboardButton("🔍 Maqola qidirish"))
    return keyboard

# /start komandasi
@dp.message_handler(commands=["start"])
async def start_command(message: types.Message):
    await message.answer("👋 Salom! Ism-familiyangizni kiriting:")

# Botni ishga tushirish
if name == "main":
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True)
