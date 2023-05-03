import mysql.connector
from datetime import date

class Zoo:
    def __init__(self, conn):
        self.conn = conn
        self.cursor = conn.cursor()

        # Création des tables
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS cages (
            id INT AUTO_INCREMENT PRIMARY KEY,
            superficie INT,
            capacite_max INT
        )
        """)
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS animaux (
            id INT AUTO_INCREMENT PRIMARY KEY,
            nom VARCHAR(255),
            race VARCHAR(255),
            id_cage INT,
            date_naissance DATE,
            pays_origine VARCHAR(255),
            FOREIGN KEY (id_cage) REFERENCES cages(id)
        )
        """)

    def ajouter_animal(self, nom, race, id_cage, date_naissance, pays_origine):
        query = """
        INSERT INTO animaux (nom, race, id_cage, date_naissance, pays_origine)
        VALUES (%s, %s, %s, %s, %s)
        """
        values = (nom, race, id_cage, date_naissance, pays_origine)
        self.cursor.execute(query, values)
        self.conn.commit()

    def supprimer_animal(self,id):
      query="DELETE FROM animaux WHERE id=%s"
      values=(id,)
      self.cursor.execute(query,tuple(values))
      self.conn.commit()

    def modifier_animal(self,id,nom=None,race=None,id_cage=None,date_naissance=None,pays_origine=None):
      query="UPDATE animaux SET "
      values=[]
      if nom is not None:
          query+="nom=%s,"
          values.append(nom)
      if race is not None:
          query+="race=%s,"
          values.append(race)
      if id_cage is not None:
          query+="id_cage=%s,"
          values.append(id_cage)
      if date_naissance is not None:
          query+="date_naissance=%s,"
          values.append(date_naissance)
      if pays_origine is not None:
          query+="pays_origine=%s,"
          values.append(pays_origine)
      query=query.rstrip(",")
      query+=" WHERE id=%s"
      values.append(id)
      self.cursor.execute(query,tuple(values))
      self.conn.commit()

    def ajouter_cage(self, superficie, capacite_max):
        query = "INSERT INTO cages (superficie, capacite_max) VALUES (%s, %s)"
        values = (superficie, capacite_max)
        self.cursor.execute(query, values)
        self.conn.commit()

    def supprimer_cage(self,id):
      query="DELETE FROM cages WHERE id=%s"
      values=(id,)
      self.cursor.execute(query,tuple(values))
      self.conn.commit()

    def modifier_cage(self,id ,superficie=None,capacite_max=None):
      query="UPDATE cages SET "
      values=[]
      if superficie is not None:
          query+="superficie=%s,"
          values.append(superficie)
      if capacite_max is not None:
          query+="capacite_max=%s,"
          values.append(capacite_max)
      query=query.rstrip(",")
      query+=" WHERE id=%s"
      values.append(id)
      self.cursor.execute(query,tuple(values))
      self.conn.commit()
        
    def afficher_animaux(self):
      self.cursor.execute("SELECT * FROM animaux")
      result=self.cursor.fetchall()
      for row in result:
          print(row)

    def afficher_animaux_par_cage(self,id_cage):
      query="SELECT * FROM animaux WHERE id_cage=%s"
      values=(id_cage,)
      self.cursor.execute(query,tuple(values))
      result=self.cursor.fetchall()
      for row in result:
          print(row)

    def calculer_superficie_totale(self):
      self.cursor.execute("SELECT SUM(superficie) FROM cages")
      result=self.cursor.fetchone()
      return result[0]

# Connexion à la base de données
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="***",
    database="Laplateforme"
)

zoo=Zoo(conn)

# Ajout de cages
zoo.ajouter_cage(1000 , 10)
zoo.ajouter_cage(2000 , 20)

# Ajout d'animaux
zoo.ajouter_animal("Simba", "Lion", 1, date(2010, 1, 1), "Afrique")
zoo.ajouter_animal("Nala", "Lionne", 1, date(2010, 2, 1), "Afrique")
zoo.ajouter_animal("Zazu", "Oiseau", 2, date(2009, 3, 1), "Afrique")

# Affichage des animaux
print("Animaux:")
zoo.afficher_animaux()

# Affichage des animaux par cage
print("Animaux dans la cage 1:")
zoo.afficher_animaux_par_cage(1)

# Calcul de la superficie totale
superficie_totale = zoo.calculer_superficie_totale()
print(f"Superficie totale: {superficie_totale}")

# Fermeture de la connexion
conn.close()