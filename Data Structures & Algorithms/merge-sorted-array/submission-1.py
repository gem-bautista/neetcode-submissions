class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        target = 0
        deleted_zero = 0
        while target in nums1 and deleted_zero < n:
            deleted_zero +=1
            nums1.remove(target)
        
        nums1 += nums2
        nums1.sort()