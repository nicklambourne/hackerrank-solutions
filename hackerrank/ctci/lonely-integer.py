#!/bin/python3


def lonely(a):
    record = []
    for item in a:
        if item not in record:
            record.append(item)
        else:
            record.remove(item)
    return record[0]


if __name__ == '__main__':
    n = int(input())

    a = list(map(int, input().rstrip().split()))

    print(lonely(a))
