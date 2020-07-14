""" This Source Code Form is subject to the terms of the Mozilla Public
  License, v. 2.0. If a copy of the MPL was not distributed with this
  file, You can obtain one at http://mozilla.org/MPL/2.0/."""
from googletrans import Translator

import aiogram
import config as cfg
import keyboard as k
from aiogram import types


transl = Translator(0)

listlang = cfg.LANGUES
bot = aiogram.Bot(token=cfg.TOKEN)
dp = aiogram.Dispatcher(bot)
mydb = cfg.mydb

print('started')



@dp.message_handler(commands=['start'])
async def process_start_command(message: aiogram.types.Message):
    mycursor = mydb.cursor()
    sql = "SELECT * FROM users WHERE id = %s"
    adr = (str(message.from_user.id),)
    mycursor.execute(sql, adr)
    myresult = mycursor.fetchall()
    print(myresult)
    if myresult is None or myresult == [] or myresult == ():
        mycursor = mydb.cursor()
        sql = "INSERT INTO users (id, lang) VALUES (%s, %s)"
        val = (str(message.from_user.id), "ru")
        mycursor.execute(sql, val)
        mydb.commit()
        await message.reply("Registred")
    else:
        await message.reply("You have already register in bot")

    await message.reply(cfg.STARTMSG)


@dp.message_handler(commands=['choose'])
async def process_start_command(message: aiogram.types.Message):
    await message.reply(cfg.CHOSEMSG, reply_markup=k.keyb)


@dp.callback_query_handler(lambda c: c.data)
async def process_callback_kb1btn1(callback_query: aiogram.types.CallbackQuery):
    if callback_query.data in cfg.LANGUES:

        lang = callback_query.data

        mycursor = mydb.cursor()
        sql = "UPDATE users SET lang = %s WHERE id = %s"
        val = (lang, str(callback_query.from_user.id))

        mycursor.execute(sql, val)
        await bot.send_message(callback_query.from_user.id, "Lang has changed to " + cfg.LANGDICT[lang])


@dp.message_handler()
async def echo_message(msg: types.Message):

    mycursor = mydb.cursor()
    sql = "SELECT * FROM users WHERE id = %s"
    adr = (msg.from_user.id,)
    mycursor.execute(sql, adr)
    myresult = mycursor.fetchall()
    lang = myresult[0][1]
    word = transl.translate(msg.text, dest=lang).text
    # a = str(str(msg.from_user.id) + str(myresult))

    await bot.send_message(msg.from_user.id, word)


if __name__ == '__main__':
    aiogram.executor.start_polling(dp)
