#!/bin/python3

import sys


def insertionSort2(n, arr):
    # Loop through items from left to right.
    for index in range(1, n):
        value = arr[index]
        comp_index = index - 1
        change_flag = False
        while comp_index >= 0:
            #print("Index:", str(index), "Val:", str(value), "Comp Index:", str(comp_index), "Comp Val:", str(arr[comp_index]))
            if value > arr[comp_index]:
                change_flag = True
                break
            if comp_index == 0 and arr[0] > value:
                change_flag = True
                comp_index -= 1
                break
            comp_index -= 1
        for j in range(index, comp_index, -1):
            if j - 1 >= 0:
                arr[j] = arr[j-1]
        arr[comp_index+1] = value
        if change_flag:
            print(' '.join([str(x) for x in arr]))


if __name__ == "__main__":
    n = int(input().strip())
    arr = list(map(int, input().strip().split(' ')))
    insertionSort2(n, arr)
