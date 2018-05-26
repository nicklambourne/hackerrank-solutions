#!/bin/python3

import math


def is_prime(n):
    mx = math.ceil(math.sqrt(n))
    for i in range(2, mx):
        if n % i == 0:
            return False
    return True


if __name__ == '__main__':
    p = int(input())

    for p_itr in range(p):
        n = int(input())
        if is_prime(n):
            print('Prime')
        else:
            print('Not prime')