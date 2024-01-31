import mysql.connector

mydb = mysql.connector.connect(
  host = 'localhost',
  user = 'arpeggio',
  password = 'ItsHighMoon1200!',
  database = 'laplateforme'
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM etudiant")
mycursor.execute('')

for x in mycursor:
  print(x)