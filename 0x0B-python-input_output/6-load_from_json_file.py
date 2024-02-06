#!/usr/bin/python3
"""Save to Json"""


import json


def load_from_json_file(filename):
    """function that creates an Object from a “JSON file”

    Args:
        filename : Name of the file
    Return:
        An object of type J"SON file"
    """
    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)
