import mysql.connector

conn = mysql.connector.connect(
  host="localhost",
  user="root",
  password="...",
  database="Laplateforme"
)

mycursor = conn.cursor()
mycursor.execute("CREATE TABLE etage (id INT AUTO_INCREMENT PRIMARY KEY, nom VARCHAR(255), numero INT, superficie INT)")
mycursor.execute("CREATE TABLE salles (id INT AUTO_INCREMENT PRIMARY KEY, nom VARCHAR(255), id_etage INT, capacite INT)")


mycursor.execute("SHOW TABLES")
for x in mycursor:
  print(x)
