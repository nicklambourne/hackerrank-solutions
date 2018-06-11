#!/bin/python3

import sys


def camelcase(s):
    count = 1
    for i in s:
        if i.isupper():
            count += 1
    return count


if __name__ == "__main__":
    s = input().strip()
    result = camelcase(s)
    print(result)
