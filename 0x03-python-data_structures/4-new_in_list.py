#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    """Find the element at an index"""
    length = len(my_list)

    new_list = my_list[:]

    if idx >= 0 and length > idx:
        new_list[idx] = element

    return (new_list)
