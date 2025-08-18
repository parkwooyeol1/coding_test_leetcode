class Solution:
    def reorderLogFiles(self, logs):
        letter_logs = []
        digit_logs = []

        for log in logs:
            id_, rest = log.split(" ", 1)
            if rest[0].isdigit():
                digit_logs.append(log)
            else:
                letter_logs.append((rest, id_))

        # 문자 로그 정렬: 내용 기준, 같으면 ID 기준
        letter_logs.sort(key=lambda x: (x[0], x[1]))
        # 문자 로그는 다시 id + content 붙여주기
        sorted_letter_logs = [f"{id_} {rest}" for rest, id_ in letter_logs]

        return sorted_letter_logs + digit_logs



s = Solution()
logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
print(s.reorderLogFiles(logs))