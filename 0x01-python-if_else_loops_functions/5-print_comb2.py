#!/usr/bin/python3
for i in range(0, 10):
    for k in range(0, 10):
        if k != 9:
            print("{:n}{:n}, ".format(i, k), end="")
        elif k == 9:
            print("{:n}{:n} ".format(i, k), end="")
