#!/usr/bin/python3
""" This modules contain a function that read JSON from files"""

import json


def load_from_json_file(filename):
    """ conjuring data from a JSON file """
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)
