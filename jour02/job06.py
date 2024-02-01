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
mycursor.execute('SELECT SUM(capacite) AS capacite_totale FROM salle')
mycursor.execute('')

# printing the result of the command
print('La capacité totale de toutes les salles est de', mycursor.fetchall()[0][0])