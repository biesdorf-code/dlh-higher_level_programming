#!/usr/bin/python3
"""module contains a student class"""


class Student:
    """Student that can be initialized and serialized"""

    def __init__(self, first_name, last_name, age):
        """Initializes a Student instance."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """returns a dictionary of student attributes, not JSON file"""
        return self.__dict__
