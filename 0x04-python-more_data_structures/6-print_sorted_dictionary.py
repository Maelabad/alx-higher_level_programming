#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    ord = list(a_dictionary.keys())
    ord.sort()
    for i in ord:
        print("{}: {}".format(i, a_dictionary.get(i)))
