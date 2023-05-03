import mysql.connector

conn=mysql.connector.connect(
    host="localhost",
    user="root",
    password="///",
    database="Laplateforme"
)

cursor=conn.cursor()

cursor.execute("SELECT * FROM etudiants")

for etudiant in cursor:
    print(etudiant)

cursor.close()
conn.close()
