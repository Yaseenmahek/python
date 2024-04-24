def is_safe(matrix, row, col):

    for i in range(row):
         if matrix[i][col] == 1:
            return False
    

    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if matrix[i][j] == 1:
            return False
    
    for i, j in zip(range(row, -1, -1), range(col, len(matrix))):
        if matrix[i][j] == 1:
            return False
    
    return True

def solve_n_queens(matrix, row):


    if row == len(matrix):
        return True
    
    
    for col in range(len(matrix)):
        if is_safe(matrix, row, col):
            
            matrix[row][col] = 1
            
        
            if solve_n_queens(matrix, row + 1):
                return True
            matrix[row][col] = 0
    
    return False

def print_matrix(matrix):
    """
    Print the matrix.
    """
    for row in matrix:
        print(" ".join(map(str, row)))


matrix = [[0] * 8 for _ in range(8)]


if solve_n_queens(matrix, 0):
    print("Solution found:")
    print_matrix(matrix)
else:
    print("No solution exists.")