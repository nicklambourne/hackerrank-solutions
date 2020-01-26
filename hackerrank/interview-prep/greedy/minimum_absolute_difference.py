#!/bin/python3


import os


# Complete the minimumAbsoluteDifference function below.
def minimum_absolute_difference(arr):
    if len(arr) < 2:
        return 0
    array = sorted(arr)
    min_diff = abs(array[0] - array[1])
    for index, value in enumerate(array[:-1]):
        difference = abs(array[index] - array[index + 1])
        if difference == 0:
            return 0
        elif difference < min_diff:
            min_diff = difference
    return min_diff


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = minimum_absolute_difference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
