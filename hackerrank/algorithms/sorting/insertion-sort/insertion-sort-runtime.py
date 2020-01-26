#!/bin/python3

import sys

def runningTime(arr):
    count = 0
    for i in range(1, len(arr)):
        j = i-1
        key = arr[i]
        while (j >= 0) and (arr[j] > key):
            arr[j + 1] = arr[j]
            j -= 1
            count += 1
        arr[j + 1] = key
    print(count)

if __name__ == "__main__":
    n = int(input().strip())
    arr = list(map(int, input().strip().split(' ')))
    result = runningTime(arr)
    print(result)
