#!/usr/bin/python3
""" This module contains a Square class"""


class Square:
    """ This class holds the area"""

    def __init__(self, size=0, position=(0, 0)):
        """This method initializes the instance"""

        self.size = size
        self.position = position

    @property
    def size(self):
        """" this method is used to retrieve the size, private"""
        return self.__size

    @size.setter
    def size(self, value):
        """sets this attribute, raises exceptions as needed"""
        if isinstance(value, int) is not True:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """ this method is a getter for position, a private instance attr"""
        return self.__position

    @position.setter
    def position(self, position):
        """ This method sets the value o position as tuples, and raises exeptions"""
        if not isinstance(position, tuple) or \
                len(position) != 2 or \
                not isinstance(position[0], int) or \
                not isinstance(position[1], int) or \
                position[0] < 0 or position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position

    def area(self):
        """ Area of this instance of square"""
        return self.size ** 2

    def my_print(self):
        """prints a rectangle that should look like a # square

        new lines and spaces represet y and x position
        """
        if self.size == 0:
            print()
        else:
            for y in range(self.__position[1]):
                print()
            for i in range(self.size):
                for x in range(self.__position[0]):
                    print(" ", end="")
                for j in range(self.size):
                    print("#", end="")
                print()
