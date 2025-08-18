from collections import Counter
class Solution:
    def topKFrequent(self, nums, k):
        result = []
        counter = Counter(nums)
        for i in range(k):
            a = counter.most_common(k)[i][0]
            result.append(a)


        return result
s = Solution()
nums = [1,1,1,2,2,3]
k = 2
print(s.topKFrequent(nums, k))
        