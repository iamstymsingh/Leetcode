class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maximum = nums[0]
        curSum = 0

        for i in range(len(nums)):
            if curSum < 0:
                curSum = 0
            curSum += nums[i]
            maximum = max(maximum, curSum)
    
        return maximum
             