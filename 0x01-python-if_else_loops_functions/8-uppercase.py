#!/usr/python3
def islower(need="A"):
    for i in range(97, 122):
        if ord(need) == i:
            print("{}".format(True))
        else:
            print("{}".format(False))
        break


islower("a")
