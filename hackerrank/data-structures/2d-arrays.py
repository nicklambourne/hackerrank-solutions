#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hourglass_sum function below.
def hourglass_sum(arr):
    height = len(arr)
    width = len(arr[0])
    sums = []
    for y in range(height - 2):
        for x in range(width - 2):
            total = arr[y][x] + arr[y][x+1] + arr[y][x+2] + \
                    arr[y+1][x+1] + \
                    arr[y+2][x] + arr[y+2][x+1] + arr[y+2][x+2]
            sums.append(total)
    return max(sums)
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglass_sum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()

