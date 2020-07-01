""" This Source Code Form is subject to the terms of the Mozilla Public
  License, v. 2.0. If a copy of the MPL was not distributed with this
  file, You can obtain one at http://mozilla.org/MPL/2.0/."""
import config as cfg
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

keyb = InlineKeyboardMarkup()
for i, j in cfg.LANGDICT.items():
    key = InlineKeyboardButton(j, callback_data=i)
    keyb.add(key)