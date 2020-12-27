
from google_trans_new import google_translator

import aiogram
import config as cfg
import keyboard as k
from aiogram import types

transl = google_translator()
# translate_text = transl.translate("This is a pen.", lang_tgt='ru')

listlang = cfg.LANGUES
bot = aiogram.Bot(token=cfg.TOKEN)
dp = aiogram.Dispatcher(bot)
mydb = cfg.mydb

print('started')


@dp.message_handler(commands=['start'])  # регистрация в боте
async def process_start_command(message: aiogram.types.Message):
    mycursor = mydb.cursor()

    myresult = mycursor.execute("""SELECT * FROM users
                WHERE id = ? """, (str(message.from_user.id),)).fetchall()
    # mycursor.execute(sql, adr)
    # myresult = mycursor.fetchall()
    print(myresult)
    if myresult is None or myresult == [] or myresult == ():
        mycursor = mydb.cursor()
        mycursor.execute("""INSERT INTO users (id, lang) VALUES (?, ?)""", (str(message.from_user.id), "ru")).fetchall()
        # sql = "INSERT INTO users (id, lang) VALUES (%s, %s)"
        # val = (str(message.from_user.id), "ru")
        #  mycursor.execute(sql, val)
        mydb.commit()
        await message.reply("Registred")
    else:
        await message.reply("You have already register in bot")

    await message.reply(cfg.STARTMSG)


@dp.message_handler(commands=['choose'])  # клавитура
async def process_start_command(message: aiogram.types.Message):
    await message.reply(cfg.CHOSEMSG, reply_markup=k.keyb)


@dp.callback_query_handler(lambda c: c.data)  # изменение языка
async def process_callback_kb1btn1(callback_query: aiogram.types.CallbackQuery):
    if callback_query.data in cfg.LANGUES:
        lang = callback_query.data

        mycursor = mydb.cursor()
        mycursor.execute("UPDATE users SET lang = ? WHERE id = ?", (lang, str(callback_query.from_user.id)))
        await bot.send_message(callback_query.from_user.id, "Lang has changed to " + cfg.LANGDICT[lang])


@dp.message_handler()  # основная функция перевода текста
async def echo_message(msg: types.Message):
    mycursor = mydb.cursor()
    myresult = mycursor.execute("SELECT * FROM users WHERE id = ?", (msg.from_user.id,)).fetchall()
    lang = myresult[0][1]

    word = transl.translate(msg.text, lang_tgt=lang)
    await bot.send_message(msg.from_user.id, word)


if __name__ == '__main__':
    aiogram.executor.start_polling(dp)
