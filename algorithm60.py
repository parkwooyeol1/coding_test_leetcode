class Solution:
    def twoSum(self, numbers, target):
        left = 0
        right = len(numbers) -1
        while left < right:
            k = numbers[left] + numbers[right]
            if k == target:
                return [left+1,right+1]
            elif k < target:
                left += 1
            else:
                right -= 1
        
            

s = Solution()
numbers = [3,24,50,79,88,150,345]
target = 200
print(s.twoSum(numbers, target))