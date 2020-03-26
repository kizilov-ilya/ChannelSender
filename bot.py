#!/usr/bin/env python

import asyncio

from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from scripts.config import BOT_TOKEN, ADMIN_ID
from scripts import messages
from scripts.db_manager_sql import ChannelManager

bot = Bot(BOT_TOKEN, parse_mode="HTML")
storage = MemoryStorage()
loop = asyncio.get_event_loop()
dp = Dispatcher(bot, storage=storage, loop=loop)


async def send_message(message: types.Message, *args):
    await bot.send_message(chat_id=ADMIN_ID, text=messages.text)


async def asleep_message(*args):
    await bot.send_message(chat_id=ADMIN_ID, text=messages.asleep)


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply("<b>Привет!</b>\nНапиши мне что-нибудь!")


"""
@dp.message_handler()
async def process_help_command(message: types.Message):
    await bot.send_message(chat_id=ADMIN_ID, text=message.text)
"""


@dp.message_handler(commands=['text'])
async def process_help(*args):
    await bot.send_message(ADMIN_ID, messages.send_text)


@dp.message_handler(commands=['clear'])
async def process_clear(*args):
    await ChannelManager.clean()


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=send_message, on_shutdown=send_message)

