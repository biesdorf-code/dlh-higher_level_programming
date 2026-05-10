#!/usr/bin/python3
""" Pickle test"""
import pickle


class CustomObject:
    """ Class for pickle se- deserialization"""

    def __init__(self, name, age, is_student):
        """star the stats"""
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Print the instance attributes"""
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """ instance to picklefile"""
        try:
            with open(filename, 'wb') as f:
                pickle.dump(self, f)
        except Exception:
            return None

    @classmethod
    def deserialize(cls, filename):
        """Deserialize and return"""
        try:
            with open(filename, 'rb') as f:
                obj = pickle.load(f)
            return obj
        except Exception:
            return None
