#!/usr/bin/python3
""" This module contains a Square class"""


class Square:
    """ This class holds the area"""

    def __init__(self, size=0):
        """This method initializes the instance"""
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        #: protected variable, int
        self.__size = size

    def area(self):
        """ Area of this instance of square"""
        return self.__size**2
