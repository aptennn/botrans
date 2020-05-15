from googletrans import Translator
import config as cfg
import telebot
from telebot import types

bot = telebot.TeleBot(cfg.TOKEN)
transl = Translator(0)


# translator = Translator()
# b = translator.translate('안녕하세요.', dest='ru', scr='')

@bot.message_handler(content_types=['text'])
def text(message):
    word = transl.translate(message.text).text
    bot.send_message(message.from_user.id, word)


bot.polling(none_stop=True, interval=0)
