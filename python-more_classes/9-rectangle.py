#!/usr/bin/python3
"""This module holds 1 class for task 0"""


class Rectangle:
    """ this is a classy class that could also represent a Square, will see

    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """ Initiates the rectangle"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """ Getter """
        return self.__width

    @width.setter
    def width(self, value):
        """ Setter that throw exceptions as needed """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ Getter """
        return self.__height

    @height.setter
    def height(self, value):
        """ Setter that throw exceptions as needed """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """method to return the area of the rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """method to return the perimeter of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Returns a string using some symbol"""
        if self.__width == 0 or self.__height == 0:
            return ""
        rows = []
        for i in range(self.__height):
            rows.append(str(self.print_symbol) * self.__width)
        return "\n".join(rows)

    def __repr__(self):
        """Returns a representation of the rectangle... to trick eval()"""
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """Print a message when a rectangle is deleted."""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """" Compares triangles, return the largest one, area"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_2.area() > rect_1.area():
            return rect_2
        return rect_1

    @classmethod
    def square(cls, size=0):
        """returns a square sized RECTAGLE Object"""
        return cls(size, size)  # using Rectangle(size,size) nope for inher.
