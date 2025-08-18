class Solution:
    def combinationSum(self, candidates, target):
        result = []
        def dfs(start, path, total):
            if total == target:
                result.append(path[:])
                return
            elif total > target:
                return
            for i in range(start, len(candidates)):
                total += candidates[i]
                dfs(i, path + [candidates[i]], total)
                total -= candidates[i]
        dfs(0, [], 0)
        return result
s = Solution()
candidates = [2,3,6,7]
target = 7
print(s.combinationSum(candidates, target))
