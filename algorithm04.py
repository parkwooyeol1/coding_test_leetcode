from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs):
        result = defaultdict(list)
        for i in strs:
            sort_s = ''.join(sorted(i))
            result[sort_s].append(i)

        result = result.values()
        return result



s = Solution()
strs = ["eat","tea","tan","ate","nat","bat"]
print(s.groupAnagrams(strs))
