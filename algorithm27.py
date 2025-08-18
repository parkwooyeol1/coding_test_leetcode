from itertools import product
class Solution:
    def letterCombinations(self, digits):
        temp = []
        dictionary = {
            '2' : 'abc',
            '3' : 'def',
            '4' : 'ghi',
            '5' : 'jkl',
            '6' : 'mno',
            '7' : 'pqrs',
            '8' : 'tuv',
            '9' : 'wxyz'
        }
        for i in digits:
            if i in dictionary:
                temp.append(dictionary[i])
        if not temp:
            result = []
        else:
            result = [''.join(i) for i in product(*temp)]
 
        return result