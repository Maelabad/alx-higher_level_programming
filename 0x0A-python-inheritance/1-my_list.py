#!/usr/bin/python3
"""Define a MyList class"""


class MyList(list):
    """ Class that instanciate and print a list"""

    def print_sorted(self):
        """print a sorted list"""
        sorted_list = sorted(self)
        print(sorted_list)
