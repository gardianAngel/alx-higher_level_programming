#!/usr/bin/python3
# 8-uppercase.py

def uppercase(string):
    """print a string in uppercase followed by a new line"""
    for i in string:
        if i in range(97, 122):
            i = chr(ord(i) - 32)
        print("{}\n".format(i), end="")

