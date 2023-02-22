#!/usr/bin/python3

def print_last_digit(number):
    val = abs(number) % 10
    print(val, end="")
    return val
