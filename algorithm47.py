class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(6)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
class Solution:
    def minDiffInBST(self, root):
        a = None
        m = float('inf')
        def dfs(node):
            nonlocal a, m
            if not node:
                return 
            dfs(node.left)
            if a != None:
                m = min(m, node.val - a)
            a = node.val
            dfs(node.right)
        dfs(root)
        return m
s = Solution()
print(s.minDiffInBST(root))