from typing import List


def merge_sort(unsorted: List[int]) -> List[int]:
    def remerge(a: List[int], b: List[int]) -> List[int]:
        new = []
        while a or b:
            if not a:
                return new + b
            if not b:
                return new + a
            if a[0] < b[0]:
                new.append(a.pop(0))
            else:
                new.append(b.pop(0))

    length = len(unsorted)
    if length < 2:  # Base case
        return unsorted

    half = length // 2
    return remerge(merge_sort(unsorted[:half]), merge_sort(unsorted[half:]))


if __name__ == "__main__":
    test = [82, 13, 85, 7, 44, 52, 56, 81, 94, 1, 45, 96, 93, 83, 3, 55, 26, 43, 15, 99]
    print(merge_sort(test))
