#!/usr/bin/python3
def load_from_json_file(filename):
    with open(filename, 'r', encoding="utf-8") as f:
        number_char = f.read()
    return number_char
