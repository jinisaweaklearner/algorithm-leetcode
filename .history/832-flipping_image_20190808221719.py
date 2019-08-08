


def flipAndInvertImage(A):

    # flip
    flip_times = len(A[0])/2
    length = len(A[0])

    # float need to be changed into int to use in range
    for n_row in range(len(A)):
        for i in range(flip_times):
            A[n_row][i],A[n_row][length-i-1] = A[n_row][length-i-1],A[n_row][i]

    # invert
    for n_row in range(len(A)):
        for n_item in range(length):
            A[n_row][n_item] = abs(A[n_row][n_item]-1)
    print(A)
    return A


flipAndInvertImage([[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]])