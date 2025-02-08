A = [
    [1, 2, 4],
    [1, 2, 4],
    [1, 2, 4]
]

B = [
    [5, 2, 4],
    [1, 7, 4],
    [1, 2, 9]
]

result = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

for i in range(len(A)):
    for j in range(len(B[0])):
        result[i][j] = A[i][j] * B[i][j]

for row in result:
    print(row)
