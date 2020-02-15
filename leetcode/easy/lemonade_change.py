from typing import List


class Solution:
    @staticmethod
    def lemonade_change(bills: List[int]) -> bool:
        fives = 0
        tens = 0
        twenties = 0

        for bill in bills:
            if bill == 5:
                fives += 1
            if bill == 10:
                if not fives:
                    return False
                fives -= 1
                tens += 1
            if bill == 20:
                if fives and tens:
                    fives -= 1
                    tens -= 1
                elif fives >= 3:
                    fives -= 3
                else:
                    return False
                twenties += 1

        return True


if __name__ == "__main__":
    assert Solution.lemonade_change([5, 5, 5, 10, 20]) is True
    assert Solution.lemonade_change([5, 5, 10]) is True
    assert Solution.lemonade_change([10, 10]) is False
    assert Solution.lemonade_change([5, 5, 10, 10, 20]) is False
