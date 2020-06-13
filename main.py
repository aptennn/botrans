from googletrans import Translator
import mysql.connector
import aiogram
import config as cfg
import keyboard as k
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

# import telebot
# from telebot import types


transl = Translator(0)
lang = 'en'
listlang = cfg.LANGUES
bot = aiogram.Bot(token=cfg.TOKEN)
dp = aiogram.Dispatcher(bot)

print('stared')


# translator = Translator()
# b = translator.translate('안녕하세요.', dest='ru', scr='') # scr source lang , dest trans lang


@dp.message_handler(commands=['start'])
async def process_start_command(message: aiogram.types.Message):
    await message.reply(cfg.STARTMSG)


@dp.message_handler(commands=['chose'])
async def process_start_command(message: aiogram.types.Message):
    await message.reply(cfg.CHOSEMSG, reply_markup=k.keyb)


@dp.callback_query_handler(lambda c: c.data)
async def process_callback_kb1btn1(callback_query: aiogram.types.CallbackQuery):
    global lang
    if callback_query.data in cfg.LANGUES:
        lang = callback_query.data
        await bot.send_message(callback_query.from_user.id, "Lang has changed to " + cfg.LANGDICT[lang])



@dp.message_handler()
async def echo_message(msg: types.Message):
    global lang
    word = transl.translate(msg.text, dest=lang).text
    await bot.send_message(msg.from_user.id, word)


if __name__ == '__main__':
    aiogram.executor.start_polling(dp)

"""@bot.message_handler(commands=['chose'])
def setl(message):
    board = types.InlineKeyboardMarkup()  # keyborad

    for i, j in cfg.LANGDICT.items():
        langue = types.InlineKeyboardButton(text=j, callback_data=i)
        board.add(langue)

    bot.send_message(message.from_user.id, text='Choose lang', reply_markup=board)


@bot.callback_query_handler(func=lambda call: True)  # keyboard
def callback_worker(call):
    global lang
    if call.data in listlang:
        lang = call.data
        bot.send_message(call.message.chat.id, "You have choosen lang")


@bot.message_handler(content_types=['text'])
def text(message):
    word = transl.translate(message.text, dest=lang).text
    bot.send_message(message.from_user.id, word)


bot.polling(none_stop=True, interval=0)
"""
