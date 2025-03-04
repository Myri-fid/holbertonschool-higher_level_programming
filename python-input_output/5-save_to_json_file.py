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
