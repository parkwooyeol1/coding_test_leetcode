class Solution:
    def findContentChildren(self, g, s):
        g.sort()
        s.sort()
        i = j = 0
        while i < len(g) and j < len(s):
            if g[i] <= s[j]:
                i += 1
            j += 1
        return i

            
       
g = [1,2,3]
s = [3]
a = Solution()
print(a.findContentChildren(g,s))

                     
        