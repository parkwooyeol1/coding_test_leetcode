class Solution:
    def maxSubArray(self, nums):
        result = nums[0]
        k = 0
        for i in nums:
            k += i
            if k > result:
                result = k
            if k < 0:
                k = 0
        return result

s = Solution()
nums = [-2,1,-3,4,-1,2,1,-5,4]
print(s.maxSubArray(nums))