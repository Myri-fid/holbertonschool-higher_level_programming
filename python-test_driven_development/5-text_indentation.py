#!/usr/bin/python3
""" function that prints a text with 2 new lines """


def text_indentation(text):
    """ function that prints a text with 2 new lines """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    result = ""
    for char in text:
        result += char
        if char in [".", "?", ":"]:
            result += "\n\n"
    print("\n".join(line.strip() for line in result.split("\n")), end="")
