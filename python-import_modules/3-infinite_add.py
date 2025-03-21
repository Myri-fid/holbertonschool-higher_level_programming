#!/usr/bin/python3
import sys

if __name__ == "__main__":
    resultat = sum(int(arg) for arg in sys.argv[1:])
    print(resultat)
