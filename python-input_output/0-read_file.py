#!/usr/bin/python3
"""
 a function that reads a
 text file (UTF8) and prints it to stdout
"""


def read_file(filename=""):
    """
    a function that reads a
    text file (UTF8) and prints it to stdout
    """

    with open('my_file_0.txt', encoding="utf-8") as f:
        read_data = f.read()
    print(read_data)
