#!/usr/bin/python3
"""Define a read_file function"""


def write_file(filename="", text=""):
    """write_file function"""
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(text)
        return len(text)
