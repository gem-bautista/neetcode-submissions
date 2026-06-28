class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = 0
        prefix_sums = []
        for i in nums:
            total += i
            prefix_sums.append(total)

        print(prefix_sums)
        pivot = -1
        for i in range(len(prefix_sums)):
            if i == 0:
                l_sum = 0
                r_sum = prefix_sums[-1] - prefix_sums[i]
                if l_sum == r_sum:
                    pivot = i
                    break
            elif i == len(prefix_sums) - 1:
                r_sum = 0
                l_sum = prefix_sums[i - 1]
                if l_sum == r_sum:
                    pivot = i
                    break
            else:
                l_sum = prefix_sums[i - 1]
                r_sum = prefix_sums[-1] - prefix_sums[i]
                if l_sum == r_sum:
                    pivot = i
                    break
        return pivot


