class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dict1={}
        for i in range(len(nums)):
            if nums[i] in dict1:
                dict1[nums[i]]+=1
            else:
                dict1[nums[i]]=1
        for key,value in dict1.items():
            if value>(len(nums)//2):
                return key
        return -1