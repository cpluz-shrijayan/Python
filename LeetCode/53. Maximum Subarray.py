class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans=nums[0]
        tmp=0
        for i in nums:
            tmp+=i
            if tmp>ans:
                ans=tmp
            if tmp<0:
                tmp=0
        return ans
