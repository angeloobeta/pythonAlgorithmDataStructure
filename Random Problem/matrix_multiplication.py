matrix_a = [[2, 3, 4, 6],
            [7, 9, 1, 6],
            [5, 8, 1, 3]]

matrix_b = [[1, 7],
            [3, 5],
            [9, 2],
            [11, 5]]
answer = [[], [], []]
for k in range(len(matrix_b[0])):
    for i in range(len(matrix_a)):
        a = 0
        for j in range(len(matrix_b)):
            a += matrix_a[i][j] * matrix_b[j][k]
            # list comprehension here
        answer[i].append(a)
print(answer)
