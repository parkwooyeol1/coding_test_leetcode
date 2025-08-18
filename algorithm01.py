# reversed letters
"""
class Solution(object):
    def reverseString(self, s):
        reverse = []
        r = reversed(s)
        if s == None: 
            return None
        for i in r:
            reverse.append(i)
        return print(reverse)
            
s = Solution()
letter = ['h', ' ','l', 'l', 'o', 'w']
s.reverseString(letter)
"""
class Solution(object):
    def reverseString(self, s):
        if s == None: 
            return None
        s.reverse()
        return s
s = Solution()
letter = ['h', ' ','l', 'l', 'o', 'w']
s.reverseString(letter)
