class TreeNode1:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
root1 = TreeNode1(1)
root1.left = TreeNode1(3)
root1.right = TreeNode1(2)
root1.right.left = TreeNode1(5)

class TreeNode2:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
root2 = TreeNode2(2)
root2.left = TreeNode2(1)
root2.left.right = TreeNode2(4)
root2.right = TreeNode2(3)
root2.right.right = TreeNode2(7)

class Solution:
    def mergeTrees(self, root1, root2):
        def dfs(node1, node2):
            if node1 is None and node2 is None:
                return 
            if node1 is None:
                return node2
            if node2 is None:
                return node1
            merge = TreeNode1(node1.val + node2.val)
            merge.left = dfs(node1.left, node2.left)
            merge.right = dfs(node1.right, node2.right)
            return merge
        return dfs(root1,root2)


s = Solution()
print(s.mergeTrees(root1, root2))