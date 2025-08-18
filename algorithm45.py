class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
root = TreeNode(4)
root.left = TreeNode(1)
root.right = TreeNode(6)
root.left.left = TreeNode(0)
root.left.right = TreeNode(2)
root.left.right.right = TreeNode(3)
root.right.left = TreeNode(5)
root.right.right = TreeNode(7)
root.right.right.right = TreeNode(8)
class Solution:
    def bstToGst(self, root):
        node_sum = 0
        def dfs(node):
            nonlocal node_sum
            if not node:
                return
            dfs(node.right)
            node_sum += node.val
            node.val = node_sum
            dfs(node.left)
        dfs(root)
        return root
        


s = Solution()
s.bstToGst(root)