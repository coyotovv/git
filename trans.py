rows_cols_input = input("Enter number of rows and columns (e.g., 3 4): ").split()
num_rows = int(rows_cols_input[0])
num_cols = int(rows_cols_input[1])

original_matrix = []

print("Now enter the elements for each row, separated by spaces:")
for i in range(num_rows):
    row_str = input(f"Row {i + 1} (expected {num_cols} elements): ")
    new_row = list(map(int, row_str.split()))
    original_matrix.append(new_row)



print(original_matrix)

rotated_matrix_rows = int(rows_cols_input[1])
rotated_matrix_cols = int(rows_cols_input[0])

rotated_matrix = []

for x in range(rotated_matrix_rows):
    new_row2 = []
    for j in range(rotated_matrix_cols):
        new_row2.append(0)
    rotated_matrix.append(new_row2)


print(rotated_matrix)
print('rotated_matrix')