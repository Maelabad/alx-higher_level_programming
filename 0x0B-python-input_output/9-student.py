#!/usr/bin/python3
"""Define class Student"""


class Student():
    """Definition of Student class"""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        attributes = {}
        for attr in self.__dict__:
            value = getattr(self, attr)
            if isinstance(value, (list, dict, str, int, bool)):
                attributes[attr] = value
        return attributes
