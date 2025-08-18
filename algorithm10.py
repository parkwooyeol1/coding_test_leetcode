from math import prod
class Solution:
    def productExceptSelf(self, nums):
        result = []
        result_ = []
        left = 1
        nums_reverse = list(reversed(nums))
        result.append(1)
        for i in range (len(nums)-1):
            left *= nums[i]
            result.append(left)
        result.reverse()
        result_.append(result[0])
        right = 1
        for i in range (len(nums_reverse)-1):
            right *= nums_reverse[i]
            
            result_.append(result[i+1]*right)
        result_.reverse()
        return result_   
            
            




s = Solution()
nums = [1,2,3,4]
print(s.productExceptSelf(nums))





