from typing import List


class Solution:
    def max_subarray(self, nums: List[int]) -> int:
        current_max = nums[0]
        max_so_far = nums[0]

        for value in nums[1:]:
            current_max = max(value, current_max + value)
            max_so_far = max(current_max, max_so_far)

        return max_so_far
