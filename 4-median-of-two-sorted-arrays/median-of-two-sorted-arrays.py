class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums=nums1+nums2
        nums.sort()
        print(nums)
        if len(nums)%2!=0:
            median=nums[int(len(nums)/2)]
            return median
        else:
            median=(nums[int(len(nums)/2)]+nums[int(len(nums)/2)-1])/2
            return median
        