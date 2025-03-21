import csv
import json
"""
 reading data from one format (CSV) and converting
 it into another format (JSON)
"""


def convert_csv_to_json(csv_filename):
    """
    reading data from one format (CSV) and converting
    it into another format (JSON)
    """

    try:
        with open(csv_filename, mode='r', encoding='utf-8') as csvfile:
            csv_reader = csv.DictReader(csvfile)
            data = [row for row in csv_reader]
        with open('data.json', mode='w', encoding='utf-8') as jsonfile:
           json.dump(data, jsonfile, indent=4)
        return True
    except FileNotFoundError:
        print(f"Le fichier {csv_filename} est introuvable.")
        return False
    except Exception as e:
        print(f"Une erreur est survenue : {e}")
        return False
