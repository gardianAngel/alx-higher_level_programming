#!/usr/bin/python3

""" a program that imports all functions from the file calculator_1.py and handles basic operations."""


def main():
    import sys
    from calculator_1 import add,sub,mul,div
    a = int(sys.argv[2])
    b = int(sys.argv[3])
    cal_operators = ['+', '-', '*', '/']
    len_of_argv = len(sys.argv) - 1
    if len_of_argv < 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    elif sys.argv[3] not in cal_operators:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    elif sys.argv[3] == cal_operators[0]:
        print("{} {} {} = {}".format(a, sys.argv[3], b, add(a, b)))
    elif sys.argv[3] == cal_operators[1]:
        print("{} {} {} = {}".format(a, sys.argv[3], b, sub(a, b)))
    elif sys.argv[3] == cal_operators[2]:
        print("{} {} {} = {}".format(a, sys.argv[3], b, mul(a, b)))
    elif sys.argv[3] == cal_operators[3]:
        print("{} {} {} = {}".format(a, sys.argv[3], b, div(a, b)))


if __name__ == "__main__":
    main()