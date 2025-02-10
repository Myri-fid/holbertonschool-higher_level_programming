#!/usr/bin/python3
"""
a function that writes a string to a text file (UTF8) and
returns the number of characters written
"""


def write_file(filename="", text=""):
    """
    a function that writes a string to a text file (UTF8) and
    returns the number of characters written
    """

    with open('my_file_0.txt', encoding="utf-8") as f:
        read_data = f.write()
    print(read_data)
