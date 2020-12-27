
import sqlite3

TOKEN = '1062629942:AAHmJDIdRug'
STARTMSG = "Hi, i am translator bot. I use google python and google API. To change lang use /choose"
CHOSEMSG = "Choose lang"
LANGUES = ['ru', 'de', 'en']
LANGDICT = {
    'ru': 'Russian',
    'de': 'Deutch',
    'en': 'English'
}


mydb = sqlite3.connect("base.sqlite")