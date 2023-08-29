#!/usr/bin/python3
"""Define a class Square."""


class Square:

    def __init__(self, size=0):
        """Initialize a new square.

        Args:
            size (int): size of the square.
        """
        self.__size = size

    def area(self):
        """The squarred area"""
        return self.__size ** 2

    @property
    def size(self):
        """Get the size of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        """SET the size of the square

        Args:
            value: the value of the size
        """
        if type(value) is not int:
            raise TypeError('size must be an integer')

        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value
