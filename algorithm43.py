import collections
class Solution:
    def findMinHeightTrees(self, n, edge):
        graph = collections.defaultdict(list)
        for i, j in edge:
            graph[i].append(j)
            graph[j].append(i)
        leaves = []
        for i in graph.keys():
            if len(graph[i]) == 1:
                leaves.append(i)
        while n > 2:
            n -= len(leaves)
            new_leaves = []
            for leaf in leaves:
                neighbor = graph[leaf].pop()
                graph[neighbor].remove(leaf)
                if len(graph[neighbor]) == 1:
                    new_leaves.append(neighbor)
            leaves = new_leaves
        return leaves
            
n = 6
edges = [[3,0],[3,1],[3,2],[3,4],[5,4]]
s = Solution()
print(s.findMinHeightTrees(n,edges))       