#!/bin/python3

import os


# Complete the minimumSwaps function below.
def minimum_swaps(array) -> int:
    swap_count = 0
    correct_order = sorted(array)
    indexes = {v: i for i, v in enumerate(array)}

    for index, value in enumerate(array):
        correct_value = correct_order[index]
        if value != correct_value:
            current_index_of_correct_value = indexes[correct_value]
            array[current_index_of_correct_value], array[index] = array[index], array[current_index_of_correct_value] # swap them
            indexes[correct_value] = index
            indexes[value] = current_index_of_correct_value
            swap_count += 1
    return swap_count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimum_swaps(arr)

    fptr.write(str(res) + '\n')

    fptr.close()
