#!/usr/bin/python3
"""
an empty class BaseGeometry.
"""


class BaseGeometry:
    """
    an empty class BaseGeometry.
    """

    def area(self):
        """
        Raise an exception because area is not implemented
        """

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validate value as an integer greater than 0
        name: string
        """

        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")

    """
    class Rectangle that inherits from BaseGeometry.
    """


class Rectangle:
    """
    class Rectangle that inherits from BaseGeometry.
    """

    def __init__(self, width, height):
        """
        class Rectangle that inherits from BaseGeometry
        """

        self.__width = width
        self.__height = height
