#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if 0 < idx < len(my_list):
        return my_list
    new_list = my_list.copy()
    new_list.insert(idx,element)
    return new_list