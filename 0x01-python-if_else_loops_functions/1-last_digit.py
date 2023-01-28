#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lastdig = number % -10 if number < 0 else number % 10
if lastdig < 5:
    print(f"Last digit of {number} is {lastdig} and is greater than 5\n")
if lastdig == 0:
    print(f"Last digit of {number} is {lastdig} and is 0\n")
if 0 < lastdig < 6:
    print(f"Last digit of {number} is {lastdig} and is less than 6 and not 0\n")
