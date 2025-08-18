import heapq
class Solution:
    def findKthLargest(self, nums, k):
        max_heap = [-x for x in nums]
        heapq.heapify(max_heap)

        for i in range (k):
            max_ = -heapq.heappop(max_heap)
        return max_
s = Solution()
nums = [3,2,1,5,6,4]
k = 2
print(s.findKthLargest(nums, k))