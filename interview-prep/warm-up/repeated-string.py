#!/bin/python3

import os


# Complete the repeatedString function below.
def repeated_string(s: str, n: int) -> int:
    full = n // len(s)
    remainder = n % len(s)
    total = 0
    count = 0
    for char in s:
        if char == 'a':
            count += 1
    total += full * count
    for char in s[:remainder]:
        if char == 'a':
            total += 1
    return total


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeated_string(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
