import collections
import heapq
class Solution:
    def findCheapestPrice(self,n, flights, src, dst, k):
        graph = collections.defaultdict(list)
        heap = [(0, src, k + 1)]  # (price, node, stops)
        dist = [[float('inf')] * (k + 1) for _ in range(n)] # # math.inf
        for u, v, w in flights:
            graph[u].append((v, w))
        while heap:
            price, node, stops = heapq.heappop(heap)
            if node == dst:
                return price
            if stops > 0:
                for v, w in graph[node]:
                    alt = price + w
                    if alt < dist[v][stops - 1]:
                        dist[v][stops - 1] = alt
                        heapq.heappush(heap, (alt, v, stops - 1))
        return -1
      
        
n = 3
src = 7
dst = 99
k = 1
flights = [    
    [7, 10, 100],
    [10, 99, 200]
    ]
s = Solution()
print(s.findCheapestPrice(n,flights,src,dst,k))