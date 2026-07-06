class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for cur_ast in asteroids:
            while stack and stack[-1] > 0 and cur_ast < 0:
                diff = cur_ast + stack[-1]
                if diff < 0:
                    stack.pop()
                elif diff > 0:
                    cur_ast = 0
                else:
                    cur_ast = 0
                    stack.pop()

            if cur_ast:
                stack.append(cur_ast)

        return stack



