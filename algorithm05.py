class Solution:
    def longestPalindrome(self, s):
        list1 = []
        index_j = 0
        for i in range(len(s)):
            for j in range(len(s)):
                if s[i] == s[j]:
                    index_j += j
                    k = s[i:index_j + 1]
                    if k == k[::-1] and k != "":
                        list1.append(k)
                    index_j = 0
        
        long_word = max(list1, key=len)             
        return long_word
            

            
s = Solution()
k = "babad"
print(s.longestPalindrome(k))