class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sum1=0                      #kdanes algorithm 
        max1=min(nums)
        for i in range(len(nums)):
            sum1+=nums[i]
            max1=max(sum1,max1)
            if sum1<0:
                sum1=0
        return max1
        