from abc import ABC, abstractmethod

class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

    def perimeter(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.shape = radius

    def area(self):
        pass

    def perimeter(self):
        pass

class Rectangle(Shape):
    def area(self):
        pass

    def perimeter(self):
        pass
