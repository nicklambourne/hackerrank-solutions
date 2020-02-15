from typing import List, Tuple


def gather() -> Tuple[int]:
    _ = int(input())
    values = map(int, input().split(' '))
    return tuple(values)


def max_array_sum(array: List[int]) -> int:
    include = 0
    exclude = 0

    # Move along array element by element
    for element in array:
        # If including the previous element means a higher total, include that
        new_exclude = max(include, exclude)
        # Work out the total including the current element but excluding the previous
        include = exclude + element
        # Set the exclusion value for the next iteration
        exclude = new_exclude

    return max(include, exclude)


if __name__ == "__main__":
    # print(mas([3, 7, 4, 6, 5, 9]))
    assert max_array_sum([3, 7, 4, 6, 5]) == 13
    assert max_array_sum([2, 1, 5, 8, 4]) == 11
