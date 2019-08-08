def flipAndInvertImage(A):

    # # flip
    # flip_times = len(A[0])/2
    # length = len(A[0])

    # # float need to be changed into int to use in range
    
    # for n_row in range(len(A)):
    #     for i in range(flip_times):
    #         A[n_row][i],A[n_row][length-i-1] = A[n_row][length-i-1],A[n_row][i]

    # # invert
    # for n_row in range(len(A)):
    #     for n_item in range(length):
    #         A[n_row][n_item] = abs(A[n_row][n_item]-1)
    # print(A)
    # return A

    # range vs xrange
    # https://www.geeksforgeeks.org/range-vs-xrange-python/

    for row in A:
        for i in range((len(row) + 1) / 2):
            """
            In Python, the shortcut row[~i] = row[-i-1] = row[len(row) - 1 - i]
            helps us find the i-th value of the row, counting from the right.
            """
            row[i], row[~i] = abs(row[~i]-1), abs(row[i]-1)
    print(A)
    return A




flipAndInvertImage([[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]])