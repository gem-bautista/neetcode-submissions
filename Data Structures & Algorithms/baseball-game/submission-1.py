class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []

        for ch in operations:

            if ch == "C":
                stack.pop()
            elif ch == "D":
                prod = stack[-1] * 2
                stack.append(prod)
            elif ch == "+":
                cur_sum = stack[-2] + stack[-1]
                stack.append(cur_sum)
            else:
                stack.append(int(ch))

        return sum(stack)
