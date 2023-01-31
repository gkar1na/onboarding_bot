# coding: utf-8

from aiogram import Dispatcher

from telegram_bot.config import dp
from telegram_bot.middlewares.throttling import ThrottlingMiddleware


dp.middleware.setup(ThrottlingMiddleware())
