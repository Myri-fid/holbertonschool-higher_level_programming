#!/usr/bin/python3
"""
Documentation
"""


class Rectangle:
    """
Rectangle class empty
"""

    def __init__(self, width=0, height=0):
        """
        Initialisation de la classe Rectangle.
        """
        pass

    def width(self):
        """
        Initialisation de la classe Rectangle.
        """
        return self.__width

    def width(self, value):
        """
        Initialisation de la classe Rectangle.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    def height(self):
        """
        Initialisation de la classe Rectangle.
        """
        return self.__height

    def height(self, value):
        """
        Initialisation de la classe Rectangle.
        """

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value
