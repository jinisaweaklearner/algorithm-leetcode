

S = '(()())(())'

left = 0
right = 0
first = 0
string = list(S)

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
        first = index_number + 1

print('result',''.join(string))


