from typing import List, Tuple


def gather() -> Tuple[int, List[int]]:
    n = int(input())
    ranks = []
    for _ in range(n):
        ranks.append(int(input()))
    return n, ranks


def candies(ranks: List[int], n: int) -> int:
    candy_counts = [1] * n
    # 1st pass: go left to right
    for index in range(1, n):
        # If rank to the left of current is smaller, take that count and add 1
        if ranks[index] > ranks[index - 1]:
            candy_counts[index] = candy_counts[index] + candy_counts[index - 1]
    # 2nd pass: go right to left
    for index in range(n - 2, -1, -1):
        # If rank to the right of current is smaller and its count is bigger take
        # its count and add 1
        if ranks[index] > ranks[index + 1] and \
                candy_counts[index] <= candy_counts[index + 1]:
            candy_counts[index] = candy_counts[index + 1] + 1

    return sum(candy_counts)


if __name__ == "__main__":
    assert candies([1, 2, 2], 3) == 4
