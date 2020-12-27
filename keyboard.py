
import lang as dictL
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

inboard = InlineKeyboardMarkup(row_width=2)
keys = []
for i, j in dictL.LANGUAGES.items():
    key = InlineKeyboardButton(j, callback_data=i+".in")
    keys.append(key)

for i in range(len(keys) // 2):
    inboard.add(keys[i], keys[len(keys) - i - 1])


outboard = InlineKeyboardMarkup(row_width=2)
keys = []
for i, j in dictL.LANGUAGES.items():
    key = InlineKeyboardButton(j, callback_data=i+".out")
    keys.append(key)

for i in range(len(keys) // 2):
    outboard.add(keys[i], keys[len(keys) - i - 1])

keyboard2 = InlineKeyboardMarkup()
key = InlineKeyboardButton("input", callback_data="input")
key2 = InlineKeyboardButton("output", callback_data="output")
keyboard2.add(key)
keyboard2.add(key2)