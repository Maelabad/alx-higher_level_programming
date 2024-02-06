#!/usr/bin/python3
"""Define a fonction to add atttributes"""


def add_attribute(obj, attr, value):
    """ Add a new attribute to an object.
    Parameters:
    - obj: The object to which we want to add attribute.
    - attr: The name of the new attribute.
    - value: Value of the new attribute.

    Raises: TypeError: If the object cannot have a new attribute.
    """
    if hasattr(obj, '__dict__') or (hasattr(type(obj), '__slots__') and
                                    attr in type(obj).__slots__):
        setattr(obj, attr, value)
    else:
        raise TypeError("can't add new attribute")
