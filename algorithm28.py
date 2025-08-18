from itertools import combinations
class Solution:
    def combine(self, n, k) :
        temp = []
        result = []
        for i in range(1, n+1):
            temp.append(i)
        
        combi  = combinations(temp, k)
        for i in combi:
            result.append(list(i))

        return result

s = Solution()
n = 4
k = 2
print(s.combine(n, k))