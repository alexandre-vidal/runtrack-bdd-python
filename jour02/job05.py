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
mycursor.execute('SELECT SUM(superficie) AS superficie_totale FROM etage')
mycursor.execute('')

# printing the result of the command
print('La superficie de la Plateforme est de', mycursor.fetchall()[0][0], 'm²')