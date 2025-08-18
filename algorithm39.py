import collections
import heapq
class Solution:
    def findCheapestPrice(self, n, edge, src, dst, K):
        graph = collections.defaultdict(list)
        for u, v, w in edge:
            graph[u].append((v, w))
        Q = [(0, src, K)]
        while Q:
            price, node, k = heapq.heappop(Q)
            if node == dst:
                return price
            if k >= 0:
                for v, w in graph[node]:
                    alt = price + w
                    heapq.heappush(Q, (alt, v, k-1))
        return -1
      
            


n = 3
src = 0
dst = 2
k = 1
flights = [[0,1,100],[1,2,100],[0,2,500]]
s = Solution()
print(s.findCheapestPrice(n,flights,src,dst,k))
