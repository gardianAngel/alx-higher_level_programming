#!/usr/bin/python3
# 7-islower.py

def islower(need='A'):
    """check for lower case characters"""
    for i in range(97, 123):
        if ord(need) == i:
            print("{}".format(True))
        else:
            print("{}".format(False))
        break

