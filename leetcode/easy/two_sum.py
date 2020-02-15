from typing import List


class Solution:
    @staticmethod
    def two_sum(nums: List[int], target: int) -> List[int]:
        cache = dict()
        for index, value in enumerate(nums):
            cache[target - value] = index

        for index, value in enumerate(nums):
            if value in cache and cache[value] != index:
                return sorted([cache[value], index])

        raise Exception


if __name__ == "__main__":
    assert Solution.two_sum([2, 7, 11, 15], 9) == [0, 1]
    assert Solution.two_sum([3, 2, 4], 6) == [1, 2]
