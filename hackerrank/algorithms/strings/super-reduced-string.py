#!/bin/python3

import os


def super_reduced_string(s):
    reduced = ''
    index = 0
    reduction_count = 0
    while index < len(s):
        if index + 1 < len(s):
            if s[index] == s[index + 1]:
                index += 1
                reduction_count += 1
            else:
                reduced += s[index]
        elif index == len(s) - 1:
            reduced += s[index]
        index += 1
    if reduced == '':
        return 'Empty String'
    elif reduction_count == 0:
        return reduced
    else:
        return super_reduced_string(reduced)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = super_reduced_string(s)

    fptr.write(result + '\n')

    fptr.close()
