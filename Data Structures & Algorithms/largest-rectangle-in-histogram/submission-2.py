class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        stack = []  # [ind,height]
        maxArea = 0

        for ind, height in enumerate(heights):
            start = ind
            while stack and height < stack[-1][1]:
                stk_ind, stk_height = stack.pop()
                maxArea = max(maxArea, stk_height * (ind - stk_ind))
                start = stk_ind
            stack.append((start, height))

        for i, h in stack:
            maxArea = max(maxArea, h * (n - i))

        return maxArea

