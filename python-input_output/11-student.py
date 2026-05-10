#!/usr/bin/python3
"""module contains a student class"""


class Student:
    """Student that can be initialized, serialized and matrix: reloaded"""

    def __init__(self, first_name, last_name, age):
        """Initializes a student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """returns a dictionary of student attributes"""

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

    def reload_from_json(self, json):
        """replaces all attributes of the Student instance from a dictionary"""

        for key, value in json.items():
            setattr(self, key, value)
