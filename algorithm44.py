class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sortedArrayToBST(self, nums):
        def recursive(start, end):
            if start > end:
                return
            m = (start + end) // 2
            root = TreeNode(nums[m])
            root.left = recursive(start, m -1)
            root.right = recursive(m +1, end)
            return root
        return recursive(0, len(nums)-1)

s = Solution()
nums = [1,2,3,4]
