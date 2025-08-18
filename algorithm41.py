class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.right.left = TreeNode(4)
root.right.right = TreeNode(5)

class Codec:
    def serialize(self, root):
        result = []
        def dfs(node):
            if node is None:
                result.append('null') 
                return
            result.append(str(node.val))            
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return ','.join(result)

    def deserialize(self, data):
        temp = data.split(',')
        index = 0
        def dfs():
            nonlocal index
            if index == len(temp):
                return
            k = temp[index]
            index += 1
            if k == 'null':
                return
            root = TreeNode(int(k))
            root.left = dfs()
            root.right = dfs()
            return root
        return dfs()
            
s = Codec()
#print(s.serialize(root))
a = '1,2,null,null,3,4,null,null,5,null,null'
print(s.deserialize(a))