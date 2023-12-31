#!/usr/bin/python3
"""Define a class Square."""


class Square:
    """Represent a square."""

    def __init__(self, size=0):
        """Initialize a new square.

        Args:
            size (int): size of the square.
        """
        self.__size = size

    def area(self):
        """The squared area"""
        return self.__size ** 2

    @property
    def size(self):
        """Get the current size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the current size of the square.

        Args:
            value: the value of the size
        """
        if type(value) is not int:
            raise TypeError('size must be an integer')

        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def my_print(self):
        """Print the square"""
        if self.__size == 0:
            print("")
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end="")
                print("")
