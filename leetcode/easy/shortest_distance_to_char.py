from typing import List


class Solution:
    @staticmethod
    def shortest_to_char(string: str, character: str) -> List[int]:
        length = len(string)
        output = [None] * length
        nearest_char = None

        for index in range(length):
            if string[index] == character:
                nearest_char = index
                output[index] = 0
            else:
                if nearest_char is not None:
                    output[index] = abs(index - nearest_char)

        nearest_char = None
        for index in range(length - 1, -1, -1):
            if string[index] == character:
                nearest_char = index
            else:
                if nearest_char is not None and output[index]:
                    output[index] = min(output[index], abs(index - nearest_char))
                elif nearest_char:
                    output[index] = abs(index - nearest_char)

        return output


if __name__ == "__main__":
    assert Solution.shortest_to_char("loveleetcode", "e") == [3, 2, 1, 0, 1, 0, 0, 1, 2, 2, 1, 0]
    assert Solution.shortest_to_char("baaa", "b") == [0,1,2,3]
