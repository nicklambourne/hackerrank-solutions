#!/bin/python3

import math
import os
import random
import re
import sys
from itertools import combinations


def divisibleSumPairs(n, k, ar):
    pairs = combinations(ar, r=2)
    matching = []
    for pair in pairs:
        if sum(pair) % k == 0:
            matching.append(pair)
    return len(matching)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    ar = list(map(int, input().rstrip().split()))

    result = divisibleSumPairs(n, k, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
