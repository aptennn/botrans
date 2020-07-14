import pymysql
TOKEN = '1062629942:AAHmJDB8iZj8FOeTY_TeLT42m17RnJIdRug'

mydb = pymysql.connect(
    host="db4free.net",
    user="rootadmain",
    passwd="fuckfuck",
    database="youtubebase2"
)

mycursor = mydb.cursor()

sql = "DELETE FROM users WHERE id = '538372234'"

mycursor.execute(sql)

mydb.commit()


print(mycursor.rowcount, "record(s) deleted")

mycursor = mydb.cursor()

sql = "SELECT * FROM users"

mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
  print(x)