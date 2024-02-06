#!/usr/bin/python3
"""Define a MyInt class"""


class MyInt(int):
    """Class MyInt"""
    def __eq__(self, other):
        """def of __eq__
        """
        return super().__ne__(other)

    def __ne__(self, other):
        """definition of __ne__ """
        return super().__eq__(other)
