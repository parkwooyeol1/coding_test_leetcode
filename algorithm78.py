class Solution:
    def hammingDistance(self, x, y):
        z = bin(x^y)
        return z.count("1")

s = Solution()
x = 1
y = 4
print(s.hammingDistance(x,y))
        