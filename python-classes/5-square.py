#!/usr/bin/python3
""" This module contains a Square class"""


class Square:
    """ This class holds the area"""

    def __init__(self, size=0):
        """This method initializes the instance"""

        self.size = size

    @property
    def size(self):
        """" this method is used to retrieve the size, private"""
        return self.__size

    @size.setter
    def size(self, value):
        """sets this attribute, raises exceptions as needed"""
        if isinstance(size, int) is not True:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """ Area of this instance of square"""
        return self.size ** 2

    def my_print(self):
        """prints a rectangle that should look like a # square"""
        if self.size == 0:
            print()
        else:
            for i in range(self.size):
                for j in range(self.size):
                    print("#", end="")
                print()
