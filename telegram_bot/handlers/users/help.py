# coding: utf-8

from loguru import logger
from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from telegram_bot.config import dp
from telegram_bot.utils.misc.throttling import rate_limit


@dp.message_handler(CommandHelp())
@rate_limit(1)
async def bot_help(message: types.Message):
    logger.info(
        f'user.id={message.from_user.id}, user.username={message.from_user.username}: '
        f'telegram_bot/handlers/users/help.bot_help()'
    )
