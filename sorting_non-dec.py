class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        n1_0 = nums1.count(0)
        n2_0 = nums2.count(0)
        nums1 = nums1[(nums1.index(0))+1:]
        nums2 = nums2[(nums2.index(0))+1:]
        nums1.append(nums2)
        while True:
            nu
        
