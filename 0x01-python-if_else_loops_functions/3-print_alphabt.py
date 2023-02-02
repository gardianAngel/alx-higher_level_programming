#!/usr/bin/python3
for ch in range(97, 123):
    if ch == 112 or ch == 113:
        continue
    print(f"{chr(ch)}", end='')