#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    l_keys = list(a_dictionary.keys())

    for values in l_keys:
        if value == a_dictionary.get(values):
            del a_dictionary[values]
    return (a_dictionary)
