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
        if s[0] in brackets.keys():
                return False
        for i in range(len(s)):
        
            if s[i] not in brackets.keys():
                stack.append(s[i])
            else:
                if len(stack) == 0:
                    return False
                elif brackets.get(s[i]) == stack[-1]:
                    stack.pop()
                else:
                    return False
        if len(stack) != 0:
            return False
        else:
            return True

