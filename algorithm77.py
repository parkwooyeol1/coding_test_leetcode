import collections
class Solution:
    def singleNumber(self, nums):
        result = 0
        for num in nums:
            result = result ^ num
        return result
s = Solution
nums = [1, 2, 1, 2, 4]
print(s.singleNumber(nums))