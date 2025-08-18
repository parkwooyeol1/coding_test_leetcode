from collections import Counter
class Solution:
    def mostCommonWord(self, paragraph, banned):
        temp = ""
        result = []
        
        for j in paragraph:
            if j.isalpha():
                temp += j
            else:
                if temp:
                    result.append(temp)
                    temp = ""
        if temp:
            result.append(temp)

        result_lower = [word.lower() for word in result]

        result = []
        for i in result_lower:
            if i not in banned:
                result.append(i)
        counter = Counter(result)          #3번 0,1,2
        most_common = counter.most_common(3)[2][0]
        return most_common
            
s = Solution()
banned = ["hit"]
paragraph = "..Bob hit a ball, the hit BALL flew far after it was hit."
print(s.mostCommonWord(paragraph, banned))
'''
def mostCommonWord(paragraph: str, banned: List[str]) -> str :
    words = [word for word in re.sub(r'[^\w]',' ',paragraph).lower().split() if word not in banned]
    counts = collections.Counter(words)
    return counts.most_common(1)[0][0]
'''
