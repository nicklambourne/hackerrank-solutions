#!/bin/python3


def rotate(a, d):
    length = len(a)
    new_list = [0] * length
    for i in range(length):
        new_index = abs((i - d) % length)
        new_list[new_index] = a[i]
    return ' '.join([str(x) for x in new_list])


if __name__ == '__main__':
    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    a = list(map(int, input().rstrip().split()))

    print(rotate(a, k))