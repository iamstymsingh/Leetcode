from typing import List


class Solution:
    def largest(self, arr : List[int]) -> int:
        largest_val = float('-inf')
        for num in arr:
            largest_val = max(largest_val, num)
        return largest_val
