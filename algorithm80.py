class Solution:
    def hammingWeight(self, n):
        count = 0
        while n:
            # 1으ㄹ 뺀 값과 AND 연산 횟수 측정
            n &= n - 1
            count += 1
        return count
s = Solution()
num = 11
print(s.hammingWeight(num))