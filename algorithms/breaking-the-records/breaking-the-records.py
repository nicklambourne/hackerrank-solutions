#!/bin/python3

import os
import sys

#
# Complete the breakingRecords function below.
#
def breakingRecords(score):
    print(score)
    start = score[0]
    mx = start
    mx_c = 0
    mn = start
    mn_c = 0
    for i in score[1:]:
        if i > mx:
            mx = i
            mx_c += 1
        if i < mn:
            mn = i
            mn_c += 1
    return(mx_c, mn_c)

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    score = list(map(int, input().rstrip().split()))

    result = breakingRecords(score)

    f.write(' '.join(map(str, result)))
    f.write('\n')

    f.close()
