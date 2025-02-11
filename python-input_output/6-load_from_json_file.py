#!/usr/bin/python3
"""
 a function that creates an Object from a “JSON file”
"""
def load_from_json_file(filename):
    """
     a function that creates an Object from a “JSON file”
    """
    with open(filename, 'r', encoding="utf-8") as f:
        number_char = f.read()
    return number_char
