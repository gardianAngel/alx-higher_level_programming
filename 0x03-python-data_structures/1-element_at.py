#!/usr/bin/python3
def element_at(my_list,idx):
    '''A function that retrives an element from a list

    Arg: 
        my_list: []
        idx: index 
    
    Returns:
        element
    '''
    if idx < 0 or idx > len(my_list):
        return None
    my_list[idx]