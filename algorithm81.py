class Solution:
    def myAtoi(self, s: str) -> int:
        i = 0
        while i < len(s) and s[i] == ' ':
            i += 1

        sign = 1 
        if i < len(s) and (s[i] == '-' or s[i] == '+'):
            if s[i] == '-':
                sign = -1
            i += 1 

        num_str = ""
        while i < len(s) and s[i].isdigit():
            num_str += s[i]
            i += 1
        
        if not num_str:
            return 0
        
        result = int(num_str) * sign
        
        MAX_INT = 2**31 - 1
        MIN_INT = -2**31
        
        if result > MAX_INT:
            return MAX_INT
        if result < MIN_INT:
            return MIN_INT
            
        return result