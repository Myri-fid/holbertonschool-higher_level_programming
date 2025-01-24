#!/usr/bin/python3
"""
Ce module fonction pour additionner deux entiers ou flot convertis en entiers.
"""


def add_integer(a, b=98):
    """
Adds two integers or floats after casting them to integers.
Returns:
The integer addition of a and b.
Raises:
TypeError: If either a or b is not an integer or float.
    """
    if isinstance(a, (int, float)) is False:
        raise TypeError("a must be an integer")
    if isinstance(b, (int, float)) is False:
        raise TypeError("b must be an integer")
    return int(a + b)
