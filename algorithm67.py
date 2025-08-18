import collections
class Solution: 
    def leastInterval(self, tasks, n):
        counts = collections.Counter(tasks)
        max_value = max(counts.values())
        max_count = 0
        for i in counts.values():
            if i == max_value:
                max_count += 1
        
        part = max_value - 1                 
        k = n + 1                      
        result = part * k + max_count  
    
        return max(len(tasks), result)
            


tasks = ["A","A","A","B","B","B","C","C","D","D"]

n = 2
s = Solution()
print(s.leastInterval(tasks,n))
