#!/usr/bin/python3
"""
Module de documentation pour rectangle.py
"""


class Rectangle:
    """
    Classe qui définit un rectangle.
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        Initialisation de la classe Rectangle.
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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
        return "\n".join([str(self.print_symbol) * self.__width
                          for _ in range(self.__height)])

    def __repr__(self):
        """
        périmètre du rectangle.
        """
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        """
        perimetre du rectangle
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2
