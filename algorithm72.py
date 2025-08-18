class Solution:
    def diffWaysToCompute(self, expression):
        res = []

        for i in range(len(expression)):
            oper = expression[i]

            if oper == "*" or oper == "-" or oper == "+":
                str1 = expression[0:i]
                str2 = expression[i+1:]

                s1 = self.diffWaysToCompute(str1)
                s2 = self.diffWaysToCompute(str2)

                for a in s1:
                    for b in s2:
                        if oper == "*":
                            res.append(int(a) * int(b))
                        if oper == "-":
                            res.append(int(a) - int(b))
                        if oper == "+":
                            res.append(int(a) + int(b))
        if len(res) == 0:
            res.append(int(expression))
        return res
expression = "2*3-4*5"
s = Solution()
print(s.diffWaysToCompute(expression))
        