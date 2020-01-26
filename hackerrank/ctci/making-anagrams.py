#!/bin/python3

from collections import Counter


def anagram(a, b):
    c_a = Counter(a)
    c_b = Counter(b)
    c_i = c_a & c_b
    intersection = sum(c_i.values())
    return (len(a) - intersection) + (len(b) - intersection)


if __name__ == '__main__':
    a = input()

    b = input()

    print(anagram(a, b))