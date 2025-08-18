class Solution:
    def isValid(self, s) :
        a = ['(', '[', '{']
        b = [')', ']', '}']
        stack = []
        for i in s:
            if i in a:
                stack.append(i)
            elif i in b:
                k = b.index(i)
                if len(stack)==0 :
                    return False
                elif stack[-1] != a[k]:
                    return False
                else:
                    stack.pop()
        return not stack
            


s = Solution()
k = "([])"
print(s.isValid(k))
# (({}[]))
            
            