#!/usr/bin/python3
"""Module contains a fucntions that writes a string to a file"""


def append_write(filename="", text=""):
    """Writes to file and returns the count of written chars"""
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
