
# Could not resolve host: github.com, but I can access it without problem #1414

def sortArrayByParity(A):
    odd = []
    even = []

    for item in A:

        if item % 2 == 0:
            even.append(item)
        else:
            odd.append(item)
    
     
    print (even+odd)
    return even+odd

sortArrayByParity([2,5,3,6,1])