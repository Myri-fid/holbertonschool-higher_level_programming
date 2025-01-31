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
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Initialisation de la classe Rectangle.
        """
        return self.__width

    @property
    def width(self, value):
        """
        Initialisation de la classe Rectangle.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Initialisation de la classe Rectangle.
        """
        return self.__height

    @property
    def height(self, value):
        """
        Initialisation de la classe Rectangle.
        """

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value
