import mysql.connector

class EmployesCRUD:
    def __init__(self, conn):
        self.conn = conn
        self.cursor = conn.cursor()

    def create(self, nom, prenom, salaire, id_service):
        query = "INSERT INTO employes (nom, prenom, salaire, id_service) VALUES (%s, %s, %s, %s)"
        values = (nom, prenom, salaire, id_service)
        self.cursor.execute(query, values)
        self.conn.commit()

    def read(self, id):
        query = "SELECT * FROM employes WHERE id = %s"
        values = (id,)
        self.cursor.execute(query, values)
        return self.cursor.fetchone()

    def update(self, id, nom=None, prenom=None, salaire=None, id_service=None):
        query = "UPDATE employes SET "
        values = []
        if nom is not None:
            query += "nom = %s,"
            values.append(nom)
        if prenom is not None:
            query += "prenom = %s,"
            values.append(prenom)
        if salaire is not None:
            query += "salaire = %s,"
            values.append(salaire)
        if id_service is not None:
            query += "id_service = %s,"
            values.append(id_service)
        query = query.rstrip(",")
        query += " WHERE id = %s"
        values.append(id)
        self.cursor.execute(query, tuple(values))
        self.conn.commit()

    def delete(self, id):
        query = "DELETE FROM employes WHERE id = %s"
        values = (id,)
        self.cursor.execute(query, values)
        self.conn.commit()

# Connexion à la base de données
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="---",
    database="Laplateforme"
)

# Création de la table employes
cursor = conn.cursor()
cursor.execute("""
CREATE TABLE employes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nom VARCHAR(255),
    prenom VARCHAR(255),
    salaire DECIMAL(10,2),
    id_service INT
)
""")

# Insertion d'employés dans la table employes
employes_crud = EmployesCRUD(conn)
employes_crud.create("Dupont", "Jean", 3500.00, 1)
employes_crud.create("Martin", "Pierre", 2500.00, 2)
employes_crud.create("Durand", "Marie", 4000.00, 1)

# Récupération des employés avec un salaire supérieur à 3000€
cursor.execute("SELECT * FROM employes WHERE salaire > 3000")
result = cursor.fetchall()
for row in result:
    print(row)

# Création de la table services
cursor.execute("""
CREATE TABLE services (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nom VARCHAR(255)
)
""")

# Insertion de services dans la table services
query = "INSERT INTO services (nom) VALUES (%s)"
values = [
    ("Informatique",),
    ("Ressources Humaines",)
]
cursor.executemany(query, values)
conn.commit()

# Récupération des employés et de leur service respectif
cursor.execute("""
SELECT e.nom, e.prenom, s.nom FROM employes e
INNER JOIN services s ON e.id_service = s.id
""")
result = cursor.fetchall()
for row in result:
    print(row)

# Mise à jour d'un employé
employes_crud.update(1, salaire=4000.00)

# Suppression d'un employé
employes_crud.delete(2)

# Fermeture de la connexion
conn.close()