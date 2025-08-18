from itertools import combinations
class Solution:
    def arrayPairSum(self, nums):
        nums.sort()
        return sum(nums[::2])
        
s = Solution()
nums = [1,4,3,2,5,6]
s.arrayPairSum(nums)