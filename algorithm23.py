class Solution:
    def numJewelsInStones(self, jewels, stones):
        count = 0
        for i in stones:
            if i in jewels:
                count +=1
        return count
    """
    def solution(j, s):
    freqs = collections.Counter(s)
    count = 0
    for char in j:
        count += freqs[char]
    return count
    """