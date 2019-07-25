

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
                need_to_remove.append(first)
                need_to_remove.append(index_number)
                first = index_number+1

        string.remove(need_to_remove)

        return ''.join(string)


removeOuterParentheses("(()())(())")
        