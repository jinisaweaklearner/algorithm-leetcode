

class Solution:
    def removeOuterParentheses(self, S: str) -> str:

        left = 0
        right = 0
        first = 0
        last = 0
        need_to_remove = []

        for index_number,each in enumerate(S):
            if each == '(':
                left += 1
            elif each == ')':
                right += 1
            
            if left != right:
                continue
            else:
                
        

        