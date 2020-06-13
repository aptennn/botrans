
import mysql.connector

TOKEN = ''
STARTMSG = "Hi, i am translator bot. I use google python and google API. To change lang use /chose"
CHOSEMSG = "Chose lang"
LANGUES = ['ru', 'de', 'en']
LANGDICT = {
    'ru': 'Russian',
    'de': 'Deutch',
    'en': 'English'
}


mydb = mysql.connector.connect(
    host="db4free.net",
    user="",
    passwd="",
    database=""
)