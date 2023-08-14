#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    maxim = 0
    for i in my_list:
        maxim = max(maxim, i)
    return maxim