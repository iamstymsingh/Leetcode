class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left, right = 0, 0
        min_window_length = float('inf')
        current_sum = 0

        for right in range(len(nums)):
            current_sum += nums[right]

            # check window validity
            while current_sum >= target:
                min_window_length = min(min_window_length, right - left + 1)
                # shrink the window
                current_sum -= nums[left]
                left += 1

        return min_window_length if min_window_length != float('inf') else 0
