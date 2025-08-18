class Solution:
    def twoSum(self, nums, target):
        result = []
        for i in range (len(nums)):
            for j in range (len(nums)-1, 0,-1):
                if nums[i] + nums[j] == target and len(result) < 2 and i!=j: 
                    result.append(i)
                    result.append(j)
        return result 
s = Solution()
nums = [3,2,4]

target = 6
print(s.twoSum(nums, target))