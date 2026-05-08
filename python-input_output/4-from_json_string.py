#!/usr/bin/python3
"""Module with a function JSON string to Python object"""
import json


def from_json_string(my_str):
    """takes a Jason string and returns a Python object"""
    return json.loads(my_str)
