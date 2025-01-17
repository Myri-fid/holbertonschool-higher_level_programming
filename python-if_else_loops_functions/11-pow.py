#!/usr/bin/python3
def pow(a, b):
    P = 1
    for i in range(1, b+1):
        P = P*a
    return P
