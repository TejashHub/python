A = [[5, 8, 3], [7, 8, 4], [2, 9, 6] ]
B = [[4, 9, 2], [3, 2, 1], [7, 2, 1] ]
result = [[0, 0, 0], [0, 0, 0], [0, 0, 0] ]

for i in range(len(A)):
    for j in range(len(B[0])):
        result[i][j] = A[i][j] + B[i][j]
        
for row in result:
    print(row)
