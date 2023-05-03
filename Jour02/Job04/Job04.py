import mysql.connector

# Connexion à la base de données
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="&&&",
    database="Laplateforme"
)

# Récupération des données de la table "salles"
cursor = conn.cursor()
cursor.execute("SELECT nom, capacite FROM salles")
result = cursor.fetchall()

# Affichage des données en console
for row in result:
    print("Nom : ", row[0])
    print("Capacité : ", row[1])
    print("--------")

# Fermeture des curseurs et de la connexion à la base de données
cursor.close()
conn.close()
