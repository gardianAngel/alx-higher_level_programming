#!/usr/bin/python3
"""Program That Prints The Result Of  Addition of All Arguments"""


def main():
    import sys
    total = 0
    len_of_argv = sys.argv[1:]

    for i in len_of_argv:
        total += int(len_of_argv[i])

    print(sum)


if __name__ == "__main__":
    main()
