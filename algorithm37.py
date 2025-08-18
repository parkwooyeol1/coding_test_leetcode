class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
root = TreeNode(5)
root.left = TreeNode(4)
root.left.left = TreeNode(1)
root.left.right = TreeNode(1)
root.right = TreeNode(5)
root.right.right = TreeNode(5)

class Solution:
    def longestUnivaluePath(self, root):
        self.length = 0
        def dfs(node):
            left_length, right_length = 0, 0
            if node is None:
                return 0
            left = dfs(node.left)
            if node.left and node.left.val == node.val:
                left_length = left + 1
            right = dfs(node.right)
            if node.right and node.right.val == node.val:
                right_length = right + 1
            self.length = max(left_length + right_length, self.length)
            return max(left_length, right_length)
        dfs(root)
        return self.length

s = Solution()
print(s.longestUnivaluePath(root))