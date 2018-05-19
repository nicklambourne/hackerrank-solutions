#!/bin/python3
import os


# Complete the solve function below.
def solve(num, blocks, day, month):
    if num < month:
        return 0
    length = month
    segments = []
    for i in range(max(num - length + 1, 1)):
        segments.append(blocks[i:i + length])
    print(segments)
    count = 0
    for segment in segments:
        if sum(segment) == day:
            count += 1
    return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = list(map(int, input().rstrip().split()))

    dm = input().split()

    d = int(dm[0])

    m = int(dm[1])

    result = solve(n, s, d, m)

    fptr.write(str(result) + '\n')

    fptr.close()
