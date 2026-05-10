#!/usr/bin/python3
"""A module for se- and deserialization. :) """
import json


def serialize_and_save_to_file(data, filename):
    """Se a Python dictionary into a file"""
    with open(filename, 'w') as f:
        json.dump(data, f)


def load_and_deserialize(filename):
    """Load and deserialize data from a file"""
    with open(filename, 'r') as f:
        return json.load(f)
