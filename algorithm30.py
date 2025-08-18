class Solution:
    def permute(self, nums):
        def backtrack(start):
            if start == len(nums):
                res.append(nums[:])
                return
            
            for i in range(start, len(nums)):
                nums[start], nums[i] = nums[i], nums[start]
                backtrack(start + 1)
                nums[start], nums[i] = nums[i], nums[start]

        res = []
        backtrack(0)
        return res
"""
def solution(nums):
    result = []
    def dfs(path):
        if len(path) == len(nums):
            result.append(path[:])
            return
        for i in range(len(nums)):
            if nums[i] not in path:
                dfs(path+[nums[i]])
    dfs([])
    return result
"""
s = Solution()
nums = [1,2,3]
s.permute(nums)