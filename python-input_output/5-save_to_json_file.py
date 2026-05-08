#!/usr/bin/python3
"""Module with a function to write an object as JSON string to a file"""
import json


def save_to_json_file(my_obj, filename):
    """takes object, writes file"""
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(my_obj, f)
