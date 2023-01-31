# coding: utf-8

from aiogram import executor

# TODO idk how install own module by "pip install -Ue ." – it doesn't work
import sys
sys.path.append('..')

from telegram_bot import handlers, middlewares
from telegram_bot.utils.set_bot_commands import set_default_commands
from telegram_bot.utils.notify_admins import on_startup_notify, on_shutdown_notify
from loguru import logger

from telegram_bot.config import dp


async def on_startup(dispatcher):
    from utils.misc import logging
    logging.setup()

    await set_default_commands(dispatcher)
    await on_startup_notify(dispatcher)


async def on_shutdown(dispatcher):
    await on_shutdown_notify(dispatcher)


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup, on_shutdown=on_shutdown)
