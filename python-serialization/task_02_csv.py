#!/usr/bin/python3
"""A module for CSV to JSON"""
import csv
import json


def convert_csv_to_json(csv_filename):
    """Convert a CSV file to JSON """
    try:
        with open(csv_filename, 'r') as f:
            reader = csv.DictReader(f)
            data = []
            for row in reader:
                print(row)
                data.append(row)

        with open('data.json', 'w') as f:
            json.dump(data, f, indent=4)

        return True
    except FileNotFoundError:
        return False
