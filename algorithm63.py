from typing import List
import collections
class Solution:
    def minWindow(self, s: str, t: str):
        need = collections.Counter(t)
        missing = len(t)
        left = start = end = 0
        for right, char  in enumerate(s, 1): # 1, A
            if need[char] > 0 :
                missing -= 1
            need[char] -= 1 # {‘A’: 0, ‘B’: 1, ‘C’: 1}
            if missing == 0:
                while left < right and need[s[left]] < 0:
                    need[s[left]] += 1
                    left += 1
                if not end or right - left <  end - start:
                    start, end = left, right
                need[s[left]] += 1
                missing += 1
                left += 1
        return s[start:end]
            

s = "bdab"
t = "ab"
a = Solution()
print(a.minWindow(s,t))