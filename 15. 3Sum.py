class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = set()
        for i in range(len(nums)-2):
            j, k = i+1, len(nums)-1
            while j < k:
                summed = nums[i] + nums[j] + nums[k]
                if summed == 0:
                    ans.add(tuple((nums[i], nums[j], nums[k])))
                
                if summed < 0:
                    j+=1
                else:
                    k-=1
        return list(ans)
