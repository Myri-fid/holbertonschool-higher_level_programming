#!/usr/bin/python3
import sys

if __name__ == "__main__":
    argc = len(sys.argv) - 1
    print("{} argument{}".format(argc, "s" if argc != 1 else ""), end="")
    print("{}".format("." if argc == 0 else ":"))
    for i in range(argc):
        print("{}: {}".format(i + 1, sys.argv[i + 1]))
