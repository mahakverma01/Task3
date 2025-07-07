def matrix_multiplication():
    A = [[1, 2], [3, 4]]
    B = [[2, 0], [1, 2]]
    result = [[0, 0], [0, 0]]

    for i in range(2):
        for j in range(2):
            for k in range(2):
                result[i][j] += A[i][k] * B[k][j]

    print("Resultant Matrix (A x B):")
    for row in result:
        print(row)

# matrix_multiplication()
if __name__ == "__main__":
    matrix_multiplication()