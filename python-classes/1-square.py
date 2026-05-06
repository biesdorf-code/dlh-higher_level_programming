#!/usr/bin/python3
""" This module contains a Square class

It is a simple class just used for learning
"""


class Square:
    """ This class holds the area

    The class holds it's private part: area
    """

    def __init__(self, size):
        """This method initializes the instance

        This is when the square learn its size for all eternity
        Args:
            size (int): is the desired size
        """
        self.__size = size
