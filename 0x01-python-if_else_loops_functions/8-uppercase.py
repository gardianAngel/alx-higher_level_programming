#!/usr/bin/python3
# 8-uppercase.py

def uppercase(string):
    """print a string in uppercase followed by a new line"""
    for i in string:
        if ord(i) in range(97, 123):
            i = chr(ord(i) - 32)
        print("{}".format(i), end="")


