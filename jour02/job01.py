# importing modules
import mysql.connector

# connecting to database
mydb = mysql.connector.connect(
  host = 'localhost',
  user = 'username',
  password = 'password',
  database = 'laplateforme'
)

# defining cursor
mycursor = mydb.cursor()

# executing MySQL command
mycursor.execute('SELECT * FROM etudiant')
mycursor.execute('')

# printing the result of the command
for x in mycursor:
  print(x)