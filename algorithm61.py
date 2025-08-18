class Solution:
    def searchMatrix(self, matrix, target):
        for i in matrix:
            if i[0] > target:
                continue
            elif i[0] < target:
                for j in i:
                    if j == target:
                        return True
                    if j > target:
                        break
            elif i[0] == target:
                return True
        return False
s = Solution()
matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
target = 5
print(s.searchMatrix(matrix, target))