from typing import List


def binary_search(values: List[int], search_value: int) -> bool:
    left = 0
    right = len(values) - 1
    mid = (right - left) // 2
    if not len(values):
        return False
    if values[mid] == search_value:
        return True
    if search_value > values[mid]:
        return binary_search(values[mid + 1:], search_value)
    else:
        return binary_search(values[:mid], search_value)


if __name__ == "__main__":
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43,
              47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    assert binary_search(primes, 99) is False
    assert binary_search(primes, 67) is True
    assert binary_search(primes, 0) is False
    assert binary_search(primes, -1) is False
    assert binary_search(primes, 2) is True
