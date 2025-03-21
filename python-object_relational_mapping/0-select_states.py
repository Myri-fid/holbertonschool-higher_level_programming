#!/usr/bin/python3
import MySQLdb
import sys

def list_states():
    """This function connects to the MySQL database and lists all states sorted by ID"""

    conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        charset="utf8"
    )

    cur = conn.cursor()

    # Exécution de la requête pour obtenir tous les états triés par ID
    cur.execute("SELECT * FROM states ORDER BY id ASC")

    # Récupération des résultats
    rows = cur.fetchall()

    # Affichage des résultats ligne par ligne
    for row in rows:
        print(row)

    # Fermeture du curseur et de la connexion
    cur.close()
    conn.close()

# Vérifie si le script est exécuté directement
if __name__ == "__main__":
    list_states()
