#!/bin/python3

import os


# Complete the countingValleys function below.
def counting_valleys(n, s):
    height = 0
    valleys = 0
    for step in s:
        if step == 'U':
            height += 1
            if height == 0:
                valleys += 1
        elif step == 'D':
            height -= 1
    return valleys


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = counting_valleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
