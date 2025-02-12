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

    data = []
    with open(csv_filename, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)
