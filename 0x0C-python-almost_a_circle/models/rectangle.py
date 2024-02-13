#!/usr/bin/python3
"""Inherit from Base class"""


from models.base import Base


class Rectangle(Base):
    """Rectangle class
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Constructor for Rectangle class.

        Args:
            width (int): Width of the rectangle.
            height (int): Height of the rectangle.
            x (int): x-coordinate of the rectangle (default is 0).
            y (int): y-coordinate of the rectangle (default is 0).
            id (int): Unique identifier (default is None).
        """
        super().__init__(id)  # Call the superclass constructor with id
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """
        Getter method for width attribute.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter method for width attribute.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """
        Getter method for height attribute.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter method for height attribute.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """
        Getter method for x attribute.
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        Setter method for x attribute.
        """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """
        Getter method for y attribute.
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        Setter method for y attribute.
        """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        self.__y = value

    def area(self):
        """Define area function
        """
        return self.__width * self.__height

    def display(self):
        """
        Display the rectangle using '#' characters, accounting
        for x and y coordinates.
        """
        # Print y rows of spaces before printing the rectangle
        for _ in range(self.y):
            print()

        # Print each row of the rectangle
        for _ in range(self.height):
            # Print x spaces before printing the '#' characters
            print(" " * self.x + "#" * self.width)

    def __str__(self):
        """Define area function

        """
        return (
            f"[Rectangle] ({self.id}) {self.__x}/{self.__y} - "
            f"{self.__width}/{self.__height}"
        )

    def update(self, *args, **kwargs):
        """
        Update the attributes of the rectangle with no-keyword arguments.

        Args:
            args (int): List of arguments on order (id, width, height, x, y).
        """
        if args:
            if len(args) > 0:
                self.id = args[0]
            if len(args) > 1:
                self.__width = args[1]
            if len(args) > 2:
                self.__height = args[2]
            if len(args) > 3:
                self.__x = args[3]
            if len(args) > 4:
                self.__y = args[4]
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """that returns the dictionary representation of a Rectangle:
            This dictionary must contain: id, width, height, x, y
        """
        dic = {'x': self.__x, 'y': self.__y, 'id': self.id,
               'height': self.__height, 'width': self.__width}
        return dic
