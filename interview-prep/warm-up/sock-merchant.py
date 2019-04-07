#!/bin/python3

import math
import os


# Complete the sockMerchant function below.
def sock_merchant(n, ar):
    counts = {}
    for element in ar:
        if element in counts.keys():
            counts[element] += 1
        else:
            counts[element] = 1
    count = 0
    for key in counts.keys():
        count += math.floor(counts[key] / 2)
    return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sock_merchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
