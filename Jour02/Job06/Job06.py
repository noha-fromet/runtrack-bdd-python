import mysql.connector

# Connexion à la base de données
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="___",
    database="Laplateforme"
)

# Exécution de la requête
cursor = conn.cursor()
cursor.execute("SELECT SUM(capacite) FROM salles")
result = cursor.fetchone()[0]
print("La capacité totale des salles est de", result)

# Fermeture de la connexion
cursor.close()
conn.close()
