import collections

class Solution:
    def maxSlidingWindow(self, nums, k):
        result = []
        q = collections.deque()
        
        for idx, num in enumerate(nums):
            # q의 왼쪽은 최대값만을 갖는다.
            while q and  q[-1] < num:
                q.pop()
            
            q.append(num)
            
            # 윈도우 크기를 초과하면 제거
            if idx >= k and nums[idx - k] == q[0]:
                q.popleft()
            
            if idx >= k - 1:
                result.append(q[0])
        
        return result

s = Solution()
nums = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3
s.maxSlidingWindow(nums, k)
            


s = Solution()
nums = [1,3,-1,-3,5,3,6,7]
k = 3
print(s.maxSlidingWindow(nums, k))