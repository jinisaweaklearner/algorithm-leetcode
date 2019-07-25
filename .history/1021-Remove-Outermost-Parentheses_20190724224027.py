

class Solution:
    def removeOuterParentheses(self, S: str) -> str:

        left = 0
        right = 0
        first = 0
        need_to_remove = []
        string = S.split()

        for index_number,each in enumerate(string):
            if each == '(':
                left += 1
            elif each == ')':
                right += 1
            
            if left != right:
                continue
            else:
                string[first] = ''
                string[index_number] = ''

        return ''.join(string)


removeOuterParentheses("(()())(())")
        