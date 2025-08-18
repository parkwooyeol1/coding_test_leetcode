class Solution:
    def getSum(self, a, b):
        MASK = 0xFFFFFFFFFFFFFFFF     # 64비트 마스크
        MAX_INT = 0x7FFFFFFFFFFFFFFF  # 64비트 최대 양수

        while b != 0:
            carry = (a & b) << 1
            a = (a ^ b) & MASK
            b = carry & MASK

        # 음수 복원
        return a if a <= MAX_INT else ~(a ^ MASK)
       


s = Solution()
a = -1
b = -2
print(s.getSum(a,b))