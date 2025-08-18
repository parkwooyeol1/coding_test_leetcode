class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(15)
root.left.left = TreeNode(3)
root.left.right = TreeNode(7)
root.right.right = TreeNode(18)

class Solution:
    def rangeSumBST(self, root, low, high):
        result = 0
        def dfs(node):
            nonlocal result
            if not node:
                return
            dfs(node.left)
            if node.val >= low and high >= node.val:
                result += node.val
            dfs(node.right)
        dfs(root)
        return result
