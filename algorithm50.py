# class Trie:
#     def __init__(self):
#         self.trie = [[[None]*26, False]]
#     def insert(self, word):
#         node = 0
#         for k in word:
#             i = ord(k) - ord('a')
#             if self.trie[node][0][i] is None:
#                 self.trie.append([[None]*26, False])
#                 self.trie[node][0][i] = len(self.trie) - 1
#             node = self.trie[node][0][i]
#         self.trie[node][1] = True

#     def search(self, word):
#         node = 0
#         for k in word:
#             i = ord(k) - ord('a')
#             if self.trie[node][0][i] is None:
#                 return False
#             node = self.trie[node][0][i]
#         return self.trie[node][1]

#     def startsWith(self, prefix):
#         node = 0
#         for k in prefix:
#             i = ord(k) - ord('a')
#             if self.trie[node][0][i] is None:
#                 return False
#             node = self.trie[node][0][i]
#         return True
# s = Trie()
# print(s.insert("can"))
# print(s.insert("car"))
# print(s.insert("cary"))
# print(s.search("apple"))
# print(s.startsWith("car"))
# #print(s.startsWith("ak"))
# print(s.search("car"))



import collections
class TrieNode:
    def __init__(self):
        self.word = False
        self.children = collections.defaultdict(TrieNode)
class Trie:
    def __init__(self):
        self.root = TrieNode()
    # 단어 삽입
    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            node = node.children[char]
        node.word = True

    # 단어 존재 여부 판별
    def search(self, word: str) -> bool:
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.word
    # 문자열로 시작 단어 존재 여부 판별
    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True
s = Trie()
print(s.insert("can"))
print(s.insert("car"))
print(s.insert("cary"))
print(s.search("apple"))
print(s.startsWith("car"))
#print(s.startsWith("ak"))
print(s.search("car"))
