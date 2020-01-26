from typing import Callable


def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair


def car(pair: Callable):
    def first(a, b):
        return a
    return pair(first)


def cdr(pair: Callable):
    def second(a, b):
        return b
    return pair(second)


if __name__ == "__main__":
    assert car(cons(3, 4)) == 3
    assert cdr(cons(3, 4)) == 4
    print("Yep ;)")