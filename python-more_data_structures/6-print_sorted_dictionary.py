#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    myKeys = list(a_dictionary.keys())
    myKeys.sort()
    for key in myKeys:
        print(f"{key}: {a_dictionary[key]}")
