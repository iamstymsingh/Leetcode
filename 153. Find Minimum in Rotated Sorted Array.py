class Solution:
    def findMin(self, nums: List[int]) -> int:
        low, high = 0, len(nums)-1
        min_val = float('inf')
        while low <= high:
            mid = low + (high - low)//2
            min_val = min(min_val, nums[mid])

            # check for sorted side
            if nums[low] <= nums[mid]:
                min_val = min(min_val, nums[low])
                low = mid+1
            else:
                min_val = min(min_val, nums[mid])
                high = mid-1
        return min_val