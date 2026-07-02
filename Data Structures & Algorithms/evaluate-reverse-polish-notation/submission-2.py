import operator
import math
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = {
            "+": operator.add,
            "-": operator.sub,
            "*": operator.mul,
            "/": operator.truediv,
        }

        stack = []

        for char in tokens:
            if char in operators and len(stack) >= 2:
                num2 = stack.pop()
                num1 = stack.pop()
                res = operators[char](int(num1), int(num2))
                stack.append(str(math.trunc(res)))
            else:
                stack.append(char)

        return int(stack[0])

