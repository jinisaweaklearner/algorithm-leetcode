"""
store value in a list
use append and pop to make sure the matching is correct

A Stack is a linear data structure that holds a linear, ordered sequence of elements.
It is an abstract data type. A Stack works on the LIFO process (Last In First Out), 
i.e., the element that was inserted last will be removed first. 
"""
class Solution(object):
    def isValid(self, s):
        # Create a pair of opening and closing parrenthesis...
        opcl = dict(('()', '[]', '{}'))
        # Create stack data structure...
        stack = []
        # Traverse each charater in input string...
        for idx in s:
            # If open parentheses are present, append it to stack...
            if idx in '([{':
                stack.append(idx)
                               
            # If the character is closing parentheses, check that the same type opening parentheses is being pushed to the stack or not...
            # If not, we need to return false...
            elif len(stack) == 0 or idx != opcl[stack.pop()]:
                return False
        # At last, we check if the stack is empty or not...
        # If the stack is empty it means every opened parenthesis is being closed and we can return true, otherwise we return false...
        return len(stack) == 0
    


class Solution(object):
    def isValid(self, s):
        valid_dict = {')':'(',  '}':'{', ']':'['}
        output = []

        for i in s:
            if i in valid_dict.values():
                output.append(i)
            elif len(output) == 0:
                return False
            else:
                # if the value is matched
                if valid_dict[i] == output[-1]:
                    output.pop()
                else:
                    return False
        return len(output) == 0
