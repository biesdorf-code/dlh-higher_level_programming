#!/usr/bin/python3
"""Module a function that returns a JSON string"""

import json


def to_json_string(my_obj):
    """function that makes JSON strings"""
    return json.dumps(my_obj)
