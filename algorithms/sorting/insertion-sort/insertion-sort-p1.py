#!/bin/python3

import sys

def print_set(s):
    l = len(s)
    for i in range(l):
        if i != l - 1:
            print(s[i], end=" ")
        else:
            print(s[i])

def insertionSort1(n, arr):
    index = n - 1
    num = arr[index]
    while num < arr[index-1]:
        arr[index] = arr[index-1]
        index -= 1
        print_set(arr)
    arr[index] = num
    print_set(arr)

if __name__ == "__main__":
    n = int(input().strip())
    arr = list(map(int, input().strip().split(' ')))
    insertionSort1(n, arr)
