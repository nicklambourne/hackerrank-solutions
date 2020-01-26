#!/bin/python3

import os
from typing import List


# Complete the jumpingOnClouds function below.
def jumping_on_clouds(c: List[int]) -> int:
    index = 0
    jump_count = 0
    while index < len(c) - 1:
        nxt_one = c[index + 1]
        if index + 2 < len(c) and c[index + 2] == 0:
            index += 2
            jump_count += 1
        elif nxt_one == 0:
            index += 1
            jump_count += 1
    return jump_count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumping_on_clouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
