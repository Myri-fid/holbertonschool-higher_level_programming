#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    newlist = []
    result = 0
    for i in range(list_length):
        try:
            result = my_list_1 / my_list_2
        except ZeroDivisionError:
            print("wrong type")
        except TypeError:
            print("wrong type")
        except IndexError:
            print("out of range")
        finally:
            print(result)
