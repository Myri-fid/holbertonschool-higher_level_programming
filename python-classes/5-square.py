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

        self.__size = size

    @property
    def size(self):
        """
        Initialisation class Square.
        Initialise l'attribut d'instance size.
        """

        return self.__size

    @size.setter
    def size(self, value):
        """
        Initialisation class Square.
        Initialise l'attribut d'instance size.
        """

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Initialisation class Square.
        Initialise l'attribut d'instance size.
        """

        return self.__size ** 2

    def my_print(self):
        """
        Initialisation class Square.
        Initialise l'attribut d'instance size.
        """

        if self.__size == 0:
            print("")
