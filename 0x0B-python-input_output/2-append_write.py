#!/usr/bin/python3
"""Append content"""


def append_write(filename="", text=""):
    """append_write definition"""
    with open(filename, 'a', encoding='utf-8') as file:
        file.write(text)
        return len(text)
