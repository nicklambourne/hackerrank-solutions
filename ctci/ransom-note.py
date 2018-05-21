#!/bin/python3

from collections import Counter


def note(magazine, ransom):
    mag_c = Counter(magazine)
    ran_c = Counter(ransom)
    intersection = sum((mag_c & ran_c).values())
    ran_length = sum(ran_c.values())
    if ran_length == intersection:
        return "Yes"
    else:
        return "No"


if __name__ == '__main__':
    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    magazine = input().rstrip().split()

    ransom = input().rstrip().split()

    print(note(magazine, ransom))