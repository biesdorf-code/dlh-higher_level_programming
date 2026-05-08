#!/usr/bin/python3
"""module contains a student class"""


class Student:
    """Student that can be initialized and serialized"""

    def __init__(self, first_name, last_name, age):
        """Initializes a student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=[]):
        """returns a dictionary of student attributes, not JSON file"""

        if not isinstance(attrs, list):
            return self.__dict__

        for item in attrs:
            if not isinstance(item, str):
                return self.__dict__

        result = {}

        for attr_name in attrs:
            if hasattr(self, attr_name):
                value = getattr(self, attr_name)
                result[attr_name] = value

        return result
