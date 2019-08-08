


def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:

    # flip
    flip_times = len(A[0])/2
    length = len(A[0])

    for n_row in range(len(A)):
        for i in range(flip_times):
            A[n_row][i],A[n_row][length-i-1] = A[n_row][length-i-1],A[n_row][i]

    # invert
    for n_row in range(len(A)):
        for n_item in range(length):
            A[n_row][n_itme] = abs(A[n_row][n_itme]-1)

    return A


flipAndInvertImage([[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]])