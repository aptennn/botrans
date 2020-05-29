import mysql.connector
TOKEN = ''
STARTMSG = "Hi, i am translator bot. I use google python and google API."
LANGUES = ['ru', 'de', 'en']
LANGDICT = {
    'Russian': 'ru',
    'Deutch': 'de',
    'English': 'en'
}
mydb = mysql.connector.connect(
    host="db4free.net",
    user="",
    passwd="",
    database=""
)