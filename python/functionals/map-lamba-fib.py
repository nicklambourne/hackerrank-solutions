cube = lambda x: x * x * x


def fibonacci(n):
    fibs = [0, 1]
    if n < 2:
        return fibs[:n-2]
    for x in range(n-2):
        fibs.append(fibs[-1]+fibs[-2])
    return fibs


if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))
