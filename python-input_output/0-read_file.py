#!/usr/bin/python3
"""Module contains a fucntions that reads a file"""


def read_file(filename=""):
    """Reads the file and prints it"""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
