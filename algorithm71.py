import collections
class Solution:
    def majorityElement(self, nums):
        counts = collections.Counter(nums)
        result = counts.most_common()[0][0]
        return result


nums = [2,2,1,1,1,2,2]
s = Solution()
print(s.majorityElement(nums))