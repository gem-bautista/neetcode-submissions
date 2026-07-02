class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 1:
            return False
        stack = []
        brackets = {
            ")": "(",
            "]": "[",
            "}": "{",
        }

        for char in s:
            if char in brackets:
                if len(stack) > 0 and stack[-1] == brackets[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)

        if len(stack) > 0:
            return False
        else:
            return True

