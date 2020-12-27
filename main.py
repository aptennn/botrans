
import aiogram
from aiogram import types
from google_trans_new import google_translator
import lang as dictL
import config as cfg
import keyboard as k

transl = google_translator()
bot = aiogram.Bot(token=cfg.TOKEN)
dp = aiogram.Dispatcher(bot)
mydb = cfg.mydb

print('started')


@dp.message_handler(commands=['start'])  # регистрация в боте
async def process_start_command(message: aiogram.types.Message):
    mycursor = mydb.cursor()

    myresult = mycursor.execute("""SELECT * FROM users
                WHERE id = ? """, (str(message.from_user.id),)).fetchall()
    print(myresult)
    if myresult is None or myresult == [] or myresult == ():
        mycursor = mydb.cursor()
        mycursor.execute("""INSERT INTO users (id, outlang, inlang) VALUES (?, ?, ?)""", \
                         (str(message.from_user.id), "ru", "en")).fetchall()
        mydb.commit()
        await message.reply("Registred")
    else:
        await message.reply("You have already register in bot")

    await message.reply(cfg.STARTMSG)



@dp.message_handler(commands=['chose'])  # клавитура
async def process_start_command(message: aiogram.types.Message):
    await message.reply(cfg.KEYMSG, reply_markup=k.keyboard2)


@dp.callback_query_handler(lambda c: c.data)  # изменение языка
async def process_callback_kb1btn1(callback_query: aiogram.types.CallbackQuery):
    print(callback_query.data)

    if callback_query.data == "input":
        await bot.send_message(callback_query.from_user.id, cfg.INMSG, reply_markup=k.inboard)
        return
    elif callback_query.data == "output":
        await bot.send_message(callback_query.from_user.id, cfg.OUTMSG, reply_markup=k.outboard)
        return

    chose = callback_query.data.split(".")

    if chose[1] == 'out':
        outLang = chose[0]

        mycursor = mydb.cursor()
        mycursor.execute("UPDATE users SET outlang = ? WHERE id = ?", (outLang, str(callback_query.from_user.id)))
        mydb.commit()
        await bot.send_message(callback_query.from_user.id, "Lang has changed to " + dictL.LANGUAGES[outLang])

    if chose[1] == 'in':
        outLang = chose[0]

        mycursor = mydb.cursor()
        mycursor.execute("UPDATE users SET inlang = ? WHERE id = ?", (outLang, str(callback_query.from_user.id)))
        mydb.commit()
        await bot.send_message(callback_query.from_user.id, "Lang has changed to " + dictL.LANGUAGES[outLang])


@dp.message_handler()  # основная функция перевода текста
async def echo_message(msg: types.Message):
    mycursor = mydb.cursor()
    myresult = mycursor.execute("SELECT outlang, inlang FROM users WHERE id = ?", (msg.from_user.id,)).fetchall()
    word = transl.translate(msg.text, lang_tgt=myresult[0][0], lang_src= myresult[0][1])
    await bot.send_message(msg.from_user.id, word)


if __name__ == '__main__':
    aiogram.executor.start_polling(dp)
