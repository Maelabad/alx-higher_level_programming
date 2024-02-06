#!/usr/bin/python3
"""Define a is_kind_of_class function"""


def is_kind_of_class(obj, a_class):
    """ Args:
        obj : The type of the object
        a_class : An object

    Returns:
        Boolean: True or false
    """
    return isinstance(obj, a_class)
