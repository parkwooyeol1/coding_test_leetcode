import collections
class Solution:
    def characterReplacement(s: str, k: int) -> int:
        left = 0
        counts = collections.Counter()
        max_len = 0

        for right in range(len(s)):
            counts[s[right]] += 1

            # 현재 윈도우에서 가장 자주 등장한 문자 수
            max_char_n = counts.most_common(1)[0][1]

            if (right - left + 1) - max_char_n > k:
                counts[s[left]] -= 1
                left += 1

            max_len = max(max_len, right - left + 1)

        return max_len
a = Solution()
s = "ABAB"
k = 2
print(a.characterReplacement(s,k))