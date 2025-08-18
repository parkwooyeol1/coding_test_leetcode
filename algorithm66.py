class Solution:
    def reconstructQueue(self, people):
        people.sort(key=lambda x: (-x[0], x[1]))
        result = []
        for i in people:
            k = i[1]
            result.insert(k, i)  
        return result

       

        
s = Solution()
people = [[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]
print(s.reconstructQueue(people))