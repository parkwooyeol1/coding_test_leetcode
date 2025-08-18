class Solution:
    def maxProfit(self, prices):
        prices = [7, 1, 5, 3, 6, 4]
        max_profit = 0
        min_val = float('inf')

        for i in range(len(prices)):
            min_val = min(min_val, prices[i])
            max_profit = max(max_profit, prices[i] - min_val)

        
        return print(max_profit)
s = Solution()
   
prices = [7,6,4,3,1]
print(s.maxProfit(prices))