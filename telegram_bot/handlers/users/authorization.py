# coding: utf-8

from loguru import logger
from aiogram import types


from telegram_bot.config import dp

from telegram_bot.config import settings
from telegram_bot.utils.misc.throttling import rate_limit


@dp.message_handler(commands=['start'])
@rate_limit(1)
async def send_welcome(message: types.Message):
    logger.info(
        f'user.id={message.from_user.id}, user.username={message.from_user.username}: '
        f'telegram_bot/handlers/users/authorization.send_welcome()'
    )
