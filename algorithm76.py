class Solution:
    def rob(self, nums):
        a = 0
        b = 0
        for i in nums:
            k = max(a, b + i)
            b = a
            a = k
        return a

        



s = Solution()
nums = [2,1,1,2]
print(s.rob(nums))