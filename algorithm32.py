import collections
class Solution:
    def findItinerary(self, tickets):
        graph = collections.defaultdict(list)
        for x, y in sorted(tickets):
            graph[x].append(y)
        visited = []
        
        def dfs(x): 
            while graph[x]:
                y = graph[x].pop(0)
                dfs(y)
            visited.append(x)
        dfs('JFK')



        return visited


s = Solution()
tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
print(s.findItinerary(tickets))
