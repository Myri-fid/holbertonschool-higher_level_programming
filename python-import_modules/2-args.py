#!/usr/bin/python3
import sys

if __name__ == "__main__":
    print("{} argument{}{}".format(argc, "s" if argc != 1 else "", "." if argc == 0 else ":"))
    for i in range(argc):
        print("{}: {}".format(i + 1, sys.argv[i + 1]))
