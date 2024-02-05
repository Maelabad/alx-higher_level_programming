#!/usr/bin/python3

class BaseGeometry():
    """BaseGeometry class"""

    def area(self):
        """Public instance method to raise an exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Public instance method to validate an integer value"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """Rectangle class inheriting from BaseGeometry"""

    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
