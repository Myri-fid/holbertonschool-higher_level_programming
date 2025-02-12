import pickle
"""
serialize and deserialize custom Python objects
using the pickle module
"""


class CustomObject:
    """
    serialize and deserialize custom Python objects
    using the pickle module
    """

    def __init__(self, name, age, is_student):
        """
        serialize and deserialize custom Python objects
        using the pickle module
        """

        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """
        serialize and deserialize custom Python objects
        using the pickle module
        """

        for attribute, value in self.__dict__.items():
            print(f"{attribute}: {value}")

    def serialize(self, filename):
        """
        serialize and deserialize custom Python objects
        using the pickle module
        """

        with open(filename, 'wb') as f:
            pickle.dump(self, f)

    @classmethod
    def deserialize(cls, filename):
        """
        serialize and deserialize custom Python objects
        using the pickle module
        """

        pass
