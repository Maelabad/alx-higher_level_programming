#!/usr/bin/python3
"""Define a class Square."""


class Square:

    def __init__(self, size=0):
        """Initialize a new square.

        Args:
            size (int): size of the square.
        """
        if type(size) is not int:
            raise TypeError('size must be an integer')

        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size

    def area(self):
        """The squared size"""
        return self.__size ** 2
