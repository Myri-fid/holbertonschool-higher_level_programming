#!/usr/bin/python3
"""  function that prints a square with the character # """


def print_square(size):
    """  function that prints a square with the character #"""

    if type(size) != int or isinstance(size, float):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    
    print(("#" * size + "\n") * size, end="")
