class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder, inorder):
        if inorder:
            index = inorder.index(preorder.pop(0))    
            node = TreeNode(inorder[index])
            node.left = self.buildTree(preorder, inorder[0:index])  
            node.right = self.buildTree(preorder, inorder[index+1:]) 
            return node


preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
s = Solution()
s.buildTree(preorder, inorder)