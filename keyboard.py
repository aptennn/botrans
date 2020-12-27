
import config as cfg
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

keyb = InlineKeyboardMarkup()
for i, j in cfg.LANGDICT.items():
    key = InlineKeyboardButton(j, callback_data=i)
    keyb.add(key)