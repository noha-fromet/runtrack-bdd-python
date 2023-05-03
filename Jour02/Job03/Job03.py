import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="===",
    database="Laplateforme"
)

cursor = conn.cursor()

# Ajouter les données à la table etage
data_etage = [
    ('RDC', 0, 500),
    ('R+1', 1, 500)
]

for row in data_etage:
    cursor.execute("INSERT INTO etage (nom, numero, superficie) VALUES (%s, %s, %s)", row)

# Ajouter les données à la table salles
data_salles = [
    ('Lounge', 1, 100),
    ('Studio Son', 1, 5),
    ('Broadcasting', 2, 50),
    ('Bocal Peda', 2, 4),
    ('Coworking', 2, 80),
    ('Studio Video', 2, 5)
]

for row in data_salles:
    cursor.execute("INSERT INTO salles (nom, id_etage, capacite) VALUES (%s, %s, %s)", row)

# Valider les changements
conn.commit()

# Afficher les données de la table etage
cursor.execute("SELECT * FROM etage")
rows = cursor.fetchall()
for row in rows:
    print(f"id: {row[0]}, nom: {row[1]}, numero: {row[2]}, superficie: {row[3]}")

# Afficher les données de la table salles
cursor.execute("SELECT * FROM salles")
rows = cursor.fetchall()
for row in rows:
    print(f"id: {row[0]}, nom: {row[1]}, id_etage: {row[2]}, capacite: {row[3]}")