#!/usr/bin/python3
"""
Module de documentation pour rectangle
"""


class Rectangle:
    """
    Class rectangle.
    """

    def __init__(self, width=0, height=0):
        """
        Initialisation de la class Rectangle.

        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        def widht self
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        def widht self
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        def height self
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        def height self
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
