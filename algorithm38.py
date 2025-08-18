class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
root = TreeNode(4)
root.left = TreeNode(3)
root.left.left = TreeNode(1)
root.left.right = TreeNode(2)
root.right = TreeNode(1)
root.right.left = TreeNode(1)
root.right.right = TreeNode(5)
class Solution:
    def invertTree(self, root):
        def dfs(node):
            if node is None:
                return
            node.left, node.right = node.right, node.left
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return root
s = Solution()
print(s.invertTree(root))
[4,7,2,3,1,9,6]