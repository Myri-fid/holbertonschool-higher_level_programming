#!/usr/bin/python3
"""
a function that writes an Object to a text
file, using a JSON representation
"""

import json
"""
a function that writes an Object to a text
file, using a JSON representation
"""


def save_to_json_file(my_obj, filename):
    """
    a function that writes an Object to a text
    file, using a JSON representation
    """

    with open(filename, 'w') as f:
        json.dump(my_obj, f)

"""
 a function that creates an Object from a “JSON file”
"""

import json
"""
 a function that creates an Object from a “JSON file”
"""


def load_from_json_file(filename):
    """
     a function that creates an Object from a “JSON file”
    """
    with open(filename, 'r') as f:
        return json.load(f)

save_to_json_file(data, "add_item.json")
