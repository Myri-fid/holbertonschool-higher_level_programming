#!/usr/bin/python3
"""
Module de documentation pour rectangle.py
"""


class Rectangle:
    """
    Classe qui définit un rectangle.
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
        attribut width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        attribut width
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        attribut height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        attribut height
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        surface du rectangle.
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        périmètre du rectangle.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """
        périmètre du rectangle.
        """
        if self.__width == 0 or self.__height == 0:
            return ""
