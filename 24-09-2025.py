
rows = int(input("Enter number of rows: "))
matrix = []

# Input matrix
for i in range(rows):
    row = list(map(int, input(f"Enter row {i+1} elements separated by comma: ").split(",")))
    matrix.append(row)

print("Matrix:", matrix)

first_diagonal = matrix[0][0]
first_row_length = len(matrix[0])

for i, row in enumerate(matrix):
    if len(row) != first_row_length or len(row) != rows:
        print("the matrix is not a identity matrix")
        break
else:
    if matrix[i][i] == first_diagonal:
        print("the matrix has same diagonal numbers")
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                if i != j and matrix[i][j] != 0:#checksthe non-diagonal elements is zero or not
                    print("but Non-diagonal element is not zero,it's not an identity matrix")
                    exit()  # Stop immediately if found
        print("the matrix is an identity matrix")
    else:
        print("the matrix is not an identity matrix")





