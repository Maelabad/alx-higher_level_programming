#!/usr/bin/python3

class MyList(list):
    """ Class that instanciate and print a list"""

    def print_sorted(self):
        sorted_list = sorted(self)
        print(sorted_list)
