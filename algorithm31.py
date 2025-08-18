class Solution:
    """def subsets(self, nums):
        def backtrack (start, path):
            result.append(path)     
            for i in range(start, len(nums)):
                backtrack(i + 1, path + [nums[i]])
        result = []
        backtrack(0,[])
        return result
        """
    def subsets(self, nums):
        res=[[]]
        for num in nums:
            res+=[curr+[num] for curr in res]
        return res
s = Solution()
nums = [1, 2, 3]
print(s.subsets(nums))