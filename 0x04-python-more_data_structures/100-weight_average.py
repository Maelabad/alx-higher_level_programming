#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    x = 0
    y = 0

    for tuple in my_list:
        x += tuple[0] * tuple[1]
        y += tuple[1]

    return (x / y)
