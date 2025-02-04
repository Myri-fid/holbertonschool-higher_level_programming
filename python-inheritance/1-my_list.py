#!/usr/bin/python3
class MyList(list):
    """
    A class that inherits from the list and
    adds a method to print the sorted list.
    """

    def print_sorted(self):
        """
        that prints the list, but sorted (ascending sort)
        """

        print(sorted(self))
