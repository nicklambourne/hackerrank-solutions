#!/bin/python3

import os
import sys
from collections import Set


def divides_from(numbers, mx):
    r = set(range(numbers[0], mx+1, numbers[0]))
    for num in numbers[1:]:
        r = r.intersection(range(num, mx+1, num))
    print(r)
    return r

def divides_into(number, s):
    for element in s:
        print("Number", str(number), "Divides", str(element))
        if element % number != 0:
            return False
    return True

def factors(number):
    factors = set()
    for i in range(2, number+1):
        if number % i == 0:
            factors.add(i)
    return factors
#
# Complete the getTotalX function below.
#
def getTotalX(a, b):
    common_factors = divides_from(a, min(b))
    Xs = set()
    for factor in common_factors:
        if divides_into(factor, b):
            Xs.add(factor)
    return len(Xs)

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    total = getTotalX(a, b)

    f.write(str(total) + '\n')

    f.close()
