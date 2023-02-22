#!/usr/bin/python3
# 8-uppercase.py

def uppercase(string):
    for i in string:
        if ord(i) in range(97, 123):
            i = chr(ord(i) - 32)
        print("{}".format(i), end="")
    print("")


