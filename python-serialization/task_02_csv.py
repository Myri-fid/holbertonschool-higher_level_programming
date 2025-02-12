import csv
import json

def convert_csv_to_json(csv_filename):
    data = []
    with open(csv_filename,'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)
