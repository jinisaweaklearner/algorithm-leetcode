

def sortArrayByParity(A):
    odd_index = []
    even_index = []

    for index_num,item in enumerate(A):

        if item % 2 == 0:
            even_index.append(index_num)
        else:
            odd_index.append(index_num)

    return A[even_index]+A[odd_index]

test = [2,5,3,6,1]
test = [2,5,3,6,1]
sortArrayByParity()