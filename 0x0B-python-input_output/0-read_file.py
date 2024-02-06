#!/usr/bin/python3
"""Define a read_file function"""

def read_file(filename=""):
    """read file function"""
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            print(line, end='')
        print()
