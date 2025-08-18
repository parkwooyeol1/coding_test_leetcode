import collections
class Solution:
    def canCompleteCircuit(self, gas, cost):
        if sum(gas) < sum(cost):
            return -1
        total = 0
        result = 0

        for i in range(len(gas)):
            total += gas[i] - cost[i]
            if total < 0:
                total = 0
                result = i + 1

        return result
gas = [1,2,3,4,5]
cost = [3,4,5,1,2]
s = Solution()
print(s.canCompleteCircuit(gas,cost))
        
