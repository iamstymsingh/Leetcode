class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = dict()
        for idx, val in enumerate(nums):
            to_find = target - val
            if to_find in seen:
                return list((idx, seen[to_find]))
            else:
                seen[val] = idx
        return -1