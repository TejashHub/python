# Solution using forloop

# A = [
#     [1, 2, 3],
#     [7, 8, 9]
# ]

# result = [
#     [0, 0],
#     [0, 0],
#     [0, 0]
# ]

# for i in range(len(A)):
#     for j in range(len(A[0])):
#         result[j][i] = A[i][j]

# for row in result:
#     print(row)


# Solution 2 using List Comprehension

A = [
    [1, 2, 3],
    [7, 8, 9]
]

result = [[A[j][i] for j in range(len(A))] for i in range(len(A[0]))]

for row in result:
    print(row) 