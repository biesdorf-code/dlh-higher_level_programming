#!/usr/bin/python3
""" This module contains a Square class

It is a simple class just used for learning
"""


class Square:
    """ This class holds the area

    The class holds it's private part: area
    """

    def __init__(self, size=0):
        """This method initializes the instance

        This is when the square learn its size for all eternity
        Args:
            size (int): is the desired size, 0 if unknown
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        #: protected variable, int
        self.__size = size
