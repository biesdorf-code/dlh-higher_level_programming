#!/usr/bin/python3
"""Module contains a fucntions that writes a string to a file"""


def write_file(filename="", text=""):
    """Writes to file and returns the count of written chars"""
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
