import json
"""
basic serialization module that adds the functionality to serialize
a Python dictionary to a JSON file and deserialize the JSON file to
recreate the Python Dictionary
"""


def serialize_and_save_to_file(data, filename):
    """
    A Python Dictionary with data
    """

    with open(filename, "w", encoding='utf-8') as f:
        json.dump(data, f)

def load_and_deserialize(filename):
    """
    The filename of the output JSON file. If the
    output file already exists it should be replaced
    """

    with open(filename, "r", encoding='utf-8') as f:
        return json.load(f)
