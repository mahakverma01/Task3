def matrix_addition():
    A = [[1, 2], [3, 4]]
    B = [[5, 6], [7, 8]]
    result = [[0, 0], [0, 0]]

    for i in range(2):
        for j in range(2):
            result[i][j] = A[i][j] + B[i][j]

    print("Resultant Matrix (A + B):")
    for row in result:
        print(row)

#Call the function
matrix_addition()
