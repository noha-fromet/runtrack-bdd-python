import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="°°°",
    database="Laplateforme"
)

cursor = conn.cursor()

# Exécuter la requête
cursor.execute("SELECT SUM(superficie) AS superficie_totale FROM etage")
result = cursor.fetchone()

# Afficher le résultat en console
superficie_totale = result[0]
print("La superficie de La Plateforme est de", superficie_totale, "m2")

cursor.close()
conn.close()
