from googletrans import Translator
import config as cfg
import telebot
from telebot import types

bot = telebot.TeleBot(cfg.TOKEN)
transl = Translator(0)
lang = 'en'
listlang = cfg.LANGUES


# translator = Translator()
# b = translator.translate('안녕하세요.', dest='ru', scr='') # scr source lang , dest trans lang
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.from_user.id, cfg.STARTMSG)


@bot.message_handler(commands=['chose'])
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
