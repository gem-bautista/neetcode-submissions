class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        output = [0] * len(temperatures)
        stack = []
        for ind, temp in enumerate(temperatures):
            while len(stack) > 0 and temp > stack[-1][0]:
                stackTemp, stackInd = stack.pop()
                output[stackInd] = ind - stackInd
            stack.append([temp, ind])
        
        return output