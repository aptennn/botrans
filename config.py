import sqlite3

TOKEN = '1062629942:AAHmJDB8iZj8FOeTY_TeLT42m17RnJIdRug'

STARTMSG = "Hi, i am translator bot. I use google python and google API. To change lang use /choose"
KEYMSG = "Choose input or output"
OUTMSG = "Choose output language"
INMSG = "Choose input language"
mydb = sqlite3.connect("base.sqlite")