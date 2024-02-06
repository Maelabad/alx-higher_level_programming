#!/usr/bin/python3
"""Define class Student"""


class Student():
    """Definition of Student class"""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs is None:
            attrs = self.__dict__.keys()

        attributes = {}
        for attr in attrs:
            if hasattr(self, attr):
                value = getattr(self, attr)
                if isinstance(value, (list, dict, str, int, bool)):
                    attributes[attr] = value
        return attributes
