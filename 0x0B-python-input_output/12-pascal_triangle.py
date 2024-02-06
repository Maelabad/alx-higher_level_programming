#!/usr/bin/python3
"""Define a special triangle"""


def pascal_triangle(n):
    "Triangle de pascal"
    if n <= 0:
        return []

    tr = [[1]]

    for i in range(1, n):
        prev = tr[-1]
        new = [1]

        for j in range(1, i):
            new.append(prev[j - 1] + prev[j])

        new.append(1)
        tr.append(new)

    return tr
