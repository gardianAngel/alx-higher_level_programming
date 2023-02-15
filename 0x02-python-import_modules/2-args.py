#!/usr/bin/python3

def main():
    """A Program That prints The Number Of And The List Of it Argument"""
    import sys

    num_of_argv = len(sys.argv[1:])
    if num_of_argv == 0:
        print("{} Argument.".format(num_of_argv))
    elif num_of_argv > 0:
        print("{} Argument:".format(num_of_argv))
        for i in range(num_of_argv):
            print("{}: {}".format(num_of_argv, sys.argv[i]))


if __name__ == "__main__":
    main()
