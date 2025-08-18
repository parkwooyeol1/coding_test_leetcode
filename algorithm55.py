# class Solution:
#     def sortColors(self, nums):
#         for i in range(len(nums)):
#             if 0 in nums[i::]:
#                 a = nums[i::].index(0)
#             else:
#                 break
#             if i>0:
#                 a+=i
#             if a > i and nums[i] != 0:
#                 nums[i], nums[a] = nums[a], nums[i]
#         for i in range(len(nums)):
#             if 1 in nums[i::]:
#                 b = nums[i::].index(1)
#             else:
#                 break
#             if i>0:
#                 b+=i
#             if b > i and nums[i] == 2:
#                 nums[i], nums[b] = nums[b], nums[i]
#         return nums

# s = Solution()
# nums = [2,0,2,0,1,1]
# print(s.sortColors(nums))


def sortColors(nums):
    red, white, blue = 0, 0, len(nums)
    while white < blue:
        if nums[white] < 1: # 1보다 작은 경우
            nums[red], nums[white] = nums[white], nums[red]
            white += 1
            red += 1
        elif nums[white] > 1: # 1보다 큰 경우
            blue -= 1
            nums[white], nums[blue] = nums[blue], nums[white] # 힌색과 파랑을 스왑
        else:
            white += 1
    return nums
nums = [2,0,2,0,1,1]
print(sortColors(nums))

