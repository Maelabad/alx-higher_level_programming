#!/usr/bin/python3
""" Define inherits_from function"""


def inherits_from(obj, a_class):
    """Args:
        obj (_type_): _description_
        a_class (_type_): _description_

    Returns:
        Boolean: True or False
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
