def transpose(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    new_matrix = []
    for i in range(cols):
        new_row = []
        for j in range(rows):
            new_row.append(matrix[j][i])
        new_matrix.append(new_row)
    return new_matrix


matrix_one = [[1, 2, 3], [4, 5, 6]]
matrix_two = transpose(matrix_one)
print(matrix_one)
print(matrix_two)
