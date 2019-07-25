

class Solution:
    def removeOuterParentheses(self, S: str) -> str:

        left = 0
        right = 0

        for each in S:
            if each == '(':
                left += 1
            elif each == ')':
                right += 1
        

        