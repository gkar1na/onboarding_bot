# coding: utf-8

from loguru import logger
from aiogram import types

from telegram_bot.config import dp
from telegram_bot.utils.misc.throttling import rate_limit

from telegram_bot.handlers.admins.authorization import read_token


@dp.message_handler()
@rate_limit(1)
async def echo(message: types.Message):
    logger.info(
        f'user.id={message.from_user.id}, user.username={message.from_user.username}: '
        f'telegram_bot/handlers/users/echo.echo()'
    )
