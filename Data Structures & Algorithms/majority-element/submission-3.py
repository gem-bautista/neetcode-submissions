class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hashmap = {}
        majority = 0
        max_count = 0
        for i in range(len(nums)):
            hashmap[nums[i]] = 1 + hashmap.get(nums[i], 0)

        for key in hashmap:
            if hashmap[key] > max_count:
                max_count = hashmap[key]
                majority = key

        return majority



        
