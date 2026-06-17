from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_dict = defaultdict(int)
        freq = [[] for i in range(len(nums) + 1)]

        for num in nums:
            count_dict[num] += 1

        for n, c in count_dict.items():
            freq[c].append(n)
            
        res = []

        for sublist in reversed(freq):
            for item in sublist:
                res.append(item)
                if len(res) == k:
                    return res