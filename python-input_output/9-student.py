#!/usr/bin/python3
"""
class Student that defines a student by name, last name et age
"""


class Student:
    """
    class Student that defines a student by name, last name et age
    """
    def __init__(self, first_name, last_name, age):
        """Instantiation with first_name, last_name and age:
        def __init__(self, first_name, last_name, age)
        """

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        function that returns the dictionary description with simple data
        structure (list, dictionary, string, integer and boolean) for JSON
        serialization of an object
        """

        return self.__dict__
