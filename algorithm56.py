from typing import List
import heapq
class Solution:
    def kCloset(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for x, y in points:
            # dist = math.sqrt((0 - x)**2 + (0 - y)**2)
            dist = x**2 + y**2 # 최적화
            heapq.heappush(heap, (dist, x, y))
        result = []
        for _ in range(k):
            (dist, x, y) = heapq.heappop(heap)
            result.append([x, y])
        return heap
            

        
        




s = Solution()
points = [[1,3],[-2,2]]
k = 1
print(s.kCloset(points, k))