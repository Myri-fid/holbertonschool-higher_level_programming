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


class Rectangle(BaseGeometry):
    """
    class Rectangle that inherits from BaseGeometry.
    """

    def __init__(self, width, height):
        """
        class Rectangle that inherits from BaseGeometry
        """
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        """
        Return the area of the rectangle
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Return a string representation of the rectangle
        """
        return f"[Rectangle] {self.__width}/{self.__height}"


"""
 class Square that inherits from Rectangle
"""


class Square(Rectangle):
    """
    class Square that inherits from Rectangle
    """

    def __init__(self, size):
        super().integer_validator("size", size)
        self.__size = size

    def area(self):
        """
        Return the area of the rectangle
        """
        return self.__size * self.__size

    def __str__(self):
        """
        Return a string representation of the rectangle
        """
        return f"[Rectangle] {self.__width}/{self.__height}"
