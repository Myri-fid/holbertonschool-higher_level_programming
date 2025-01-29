#!/usr/bin/python3
"""
Module de documentation pour 0-square.py
"""


class Square:
    """
    Dcumentation de la class Square.
    """

    def __init__(self, size=0):
        """
        Initialisation class Square.
        Initialise l'attribut d'instance size.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
