from bot import bot, dp, types
from scripts.config import ADMIN_ID
from scripts import messages
import requests


async def send_message(message: types.Message, *args):
    await bot.send_message(chat_id=ADMIN_ID, text=messages.text)


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply("<b>Привет!</b>\nНапиши мне что-нибудь!")


"""
@dp.message_handler()
async def process_help_command(message: types.Message):
    await bot.send_message(chat_id=ADMIN_ID, text=message.text)
"""


@dp.message_handler(commands=['text'])
async def process_help(message: types.Message):
    await bot.send_message(ADMIN_ID, messages.send_text)
