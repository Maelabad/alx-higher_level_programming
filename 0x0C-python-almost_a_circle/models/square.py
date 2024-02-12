#!/usr/bin/python3
"""Now the squareee!!!"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """Define the square"""
    def __init__(self, size, x=0, y=0, id=None):
        """
        Constructor for Square class.

        Args:
            size (int): Size of the square.
            x (int): x-coordinate of the square (default is 0).
            y (int): y-coordinate of the square (default is 0).
            id (int): Unique identifier (default is None).
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Getter method for size """
        return self.width

    @size.setter
    def size(self, value):
        """Setter method for size
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value <= 0:
            raise ValueError("size must be > 0")
        self.width = value

    def update(self, *args, **kwargs):
        """assigns attributes:

        *args is the list of arguments - no-keyworded arguments
            1st argument should be the id attribute
            2nd argument should be the size attribute
            3rd argument should be the x attribute
            4th argument should be the y attribute
        **kwargs can be thought of as a double pointer to a dictionary:
                key/value (keyworded arguments)
        """
        if args:
            if len(args) > 0:
                self.id = args[0]
            if len(args) > 1:
                self.size = args[1]
            if len(args) > 2:
                self.x = args[2]
            if len(args) > 3:
                self.y = args[3]
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def __str__(self):
        """Redefine the __str__ methode"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    def to_dictionary(self):
        """returns the dictionary representation of a Square:

            This dictionary must contain:id, size, x, y
        """
        dic = {'id': self.id, 'x': self.x, 'size': self.size, 'y': self.y}
        return dic
