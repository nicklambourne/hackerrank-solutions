from typing import List


class Solution:
    @staticmethod
    def letter_combinations(digits: str) -> List[str]:
        mapping = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"]
        }

        if not digits:
            return []

        old_combos = mapping[digits[0]]

        for digit in digits[1:]:
            possible_chars = mapping[digit]
            new_combos = []
            for char in possible_chars:
                for combo in old_combos:
                    new_combos.append(combo + char)
            old_combos = new_combos

        return old_combos


if __name__ == "__main__":
    assert sorted(Solution.letter_combinations("23")) == ["ad", "ae", "af", "bd", "be", "bf", "cd",
                                                          "ce", "cf"]
