class Solution:
    def merge(self, intervals):
        intervals.sort(key=lambda x: x[0])
        result = []
        for i in intervals:
            if not result or i[0] > result[-1][1]:
                result.append(i)
            else:
                result[-1][1] = max(result[-1][1], i[1])
        return result
            




s = Solution()
intervals = [[1,3],[2,6],[8,10],[15,18]]
print(s.merge(intervals))