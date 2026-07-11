class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for counter in range(0, len(nums)):
            swapped = False
            for curr_index in range(0, len(nums) - 1 - counter):
                if nums[curr_index] > nums[curr_index + 1]:
                    nums[curr_index], nums[curr_index + 1] = nums[curr_index + 1], nums[curr_index]
                    swapped = True
            if swapped == False:
                break