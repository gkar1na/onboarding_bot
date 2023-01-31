# coding: utf-8

from loguru import logger
from aiogram import types


async def read_token(message: types.Message):
    logger.info(
        f'user.id={message.from_user.id}, user.username={message.from_user.username}: '
        f'telegram_bot/handlers/admins/authorization.read_token()'
    )
