class Solution:
    @staticmethod
    def is_valid(braces: str) -> bool:
        stack = []
        match = {
            ")": "(",
            "}": "{",
            "]": "[",
        }

        opening = set(match.values())
        closing = set(match.keys())

        for brace in braces:
            if brace in opening:
                stack.append(brace)
            elif brace in closing:
                if stack and stack[-1] == match.get(brace, None):
                    stack.pop()
                else:
                    return False
            else:
                raise Exception

        if stack:  # Not empty
            return False

        return True


if __name__ == "__main__":
    assert Solution.is_valid("()") is True
    assert Solution.is_valid("([)]") is False
    assert Solution.is_valid("{[]}") is True

