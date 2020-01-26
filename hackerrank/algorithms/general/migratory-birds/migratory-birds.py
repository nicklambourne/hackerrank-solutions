#!/bin/python3

import math
import os
import random
import re
import sys


def migratoryBirds(ar):
    counts = {}
    for bird in ar:
        if bird in counts.keys():
            counts[bird] += 1
        else:
            counts[bird] = 1
    max_key = max(counts, key=counts.get)
    all_max_keys = [x for x in counts.keys() if counts[max_key] == counts[x]]
    return min(all_max_keys)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = migratoryBirds(ar)

    fptr.write(str(result) + '\n')

    fptr.close()
