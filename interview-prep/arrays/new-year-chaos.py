#!/bin/python3


# Complete the minimumBribes function below.
def minimum_bribes(q):
    move_count = 0
    for i in reversed(range(len(q))):
        if q[i] - (i+1) > 2:
            return print("Too chaotic")
        for j in range(max(0, q[i] - 2), i):
            if q[j] > q[i]:
                move_count += 1
    print(move_count)


if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        minimum_bribes(q)
