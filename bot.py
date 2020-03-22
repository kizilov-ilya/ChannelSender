#!/usr/bin/env python

import asyncio

from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from scripts.config import BOT_TOKEN

bot = Bot(BOT_TOKEN, parse_mode="HTML")
storage = MemoryStorage()
loop = asyncio.get_event_loop()
dp = Dispatcher(bot, storage=storage, loop=loop)

if __name__ == '__main__':
    from scripts.handlers import *
    executor.start_polling(dp, on_startup=send_message)