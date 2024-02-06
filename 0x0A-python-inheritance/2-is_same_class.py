#!/usr/bin/python3
"""Define a is_same_class function"""


def is_same_class(obj, a_class):
    """  Args:
        obj : The type of the object
        a_class : An object

    Returns:
        Boolean: True or false
    """
    return type(obj) is a_class
