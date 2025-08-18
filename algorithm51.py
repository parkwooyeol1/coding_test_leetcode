# 트라이 구현
import collections
from typing import List
class TrieNode:
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.word_id = -1
        self.palindrome_word_ids = []
class Trie:
    def __init__(self):
        self.root= TrieNode()
    @staticmethod
    def is_palindrome(word: str) -> bool:
        return word[::] == word[::-1]
    # 단어 삽입
    def insert(self, index, word) -> None:
        node = self.root
        # 문자를 삽입중에 펠린드롬이라면
        for i , char in enumerate(reversed(word)):
            # 문자 1개가 남았을 때도 팰린드롬이겠다.
            if self.is_palindrome(word[0:len(word) - i]):
                node.palindrome_word_ids.append(index)
            node = node.children[char]
        node.word_id = index # 삽입이 끝나면 마지막에 인덱스를 삽입
    def search(self, index, word) -> None:
        result = []
        node = self.root
        while word:
            # 판별 로직 3
            if node.word_id >= 0: # 찾으려는 단어의 팰린드롬 판별 여부 과정중에 단어가 존재하고
                if self.is_palindrome(word): # 찾으려는 단어가 팰린드롬이라면
                    result.append([index, node.word_id])
            if not word[0] in node.children:
                return result
            node = node.children[word[0]] # 다음 노드로 이동하고
            word = word[1:] # 단어를 업데이트
        # 판별로직 1
        # 단어를 끝까지 다 탐색하여 트라이 마지막 단어에 있다면
        # 그리고 그것이 자신의 인덱스와 다르다면 팰린드롬이다.
        if node.word_id >= 0 and node.word_id != index:
            result.append([index, node.word_id])
        # 판별로직 2
        # 현재 노드에서 p값이 존재한다면
        for palindrome_word_id in node.palindrome_word_ids:
            result.append([index, palindrome_word_id])
        return result
class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        trie = Trie()
        for i, word in enumerate(words):
            trie.insert(i, word)
        results = []
        for i, word in enumerate(words):
            results.extend(trie.search(i, word))
        return results
s =  Solution()
words = ["abcd","dcba","lls","s","sssll"]