class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]

        lb, ub = self.lb(nums, target), self.ub(nums, target)
        if lb == len(nums) or nums[lb] != target: # element not found
            return [-1, -1]
        else:
            return [lb, ub-1]
            

    def lb(self, nums, target) -> int:
        low, high = 0, len(nums)-1
        ans = len(nums)
        while low <= high:
            mid = low + (high - low)//2
            if nums[mid] >= target:
                ans = mid
                high = mid-1
            else:
                low = mid+1
        return ans

    def ub(self, nums, target) -> int:
        low, high = 0, len(nums)-1
        ans = len(nums)
        while low <= high:
            mid = low + (high - low)//2
            if nums[mid] > target:
                ans = mid
                high = mid-1
            else:
                low = mid+1
        return ans 