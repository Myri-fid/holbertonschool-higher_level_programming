#!/usr/bin/python3
"""
 script that adds all arguments to a Python list, and then save them to a file
"""


def save_to_json_file(my_obj, filename):
    """
    a function that writes an Object to a text
    file, using a JSON representation
    """

    with open(filename, 'w', encoding="utf-8") as f:
        json.dump(my_obj, f)


def load_from_json_file(filename):
    """
     a function that creates an Object from a “JSON file”
    """
    with open(filename, 'r', encoding="utf-8") as f:
        return json.load(f)

