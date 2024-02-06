#!/usr/bin/python3
"""Save to Json"""


def class_to_json(obj):
    """class to json"""
    attributes = {}
    for attr in dir(obj):
        # Ignore private and special attributes
        if not attr.startswith("__") and not callable(getattr(obj, attr)):
            value = getattr(obj, attr)
            if isinstance(value, (list, dict, str, int, bool)):
                attributes[attr] = value
    return attributes
