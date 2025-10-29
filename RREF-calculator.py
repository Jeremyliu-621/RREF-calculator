"""

A calculator that turns any nxm matrix into it's RREF form!
Based on our learnings from UofT's First Year Engineering linear algebra course!
Includes pivots and gaussian elimination.

Jeremy Liu
10/29/2025

"""

# importing modules
import time

def main():
    matrix_list, num_rows, num_columns = get_matrix()
    matrix = rref(matrix_list, num_rows, num_columns)
    print("Your final matrix in RREF")
    for _ in matrix:
        print(_)

def get_matrix():

    # initializing the matrix with a list
    # will contain the number of rows as lists

    matrix_list = []

    num_rows, num_columns = input(
        "How large should the matrix be? Give me two numbers seperated by a comma (_,_),\n " \
        "the first being the number of rows of the matrix, and the second being the number of columns.\n " \
        "Enter here: "
        ).split(",")
    
    num_rows = int(num_rows)
    num_columns = int(num_columns)

    for _ in range(num_rows):
        for _ in range(num_columns):
            print("[ ]", end="")
        print()

    print("Now enter the entries row by row!")

    for element in range(num_rows):
        row_nums = input(f"Input all numbers for row {element+1}. Input {num_columns} number total, separated by commas (_,_,...,_): ").split(",")
        
        # the list form of the "row_nums" strs are converted to floats, then appended to a list
        num_list = []
        for num in row_nums:
            num_list.append(float(num))
        # list is then appended to the matrix_list
        matrix_list.append(num_list)

    print("Your matrix: ")
    for row in matrix_list:
        print(row)

    return matrix_list, num_rows, num_columns

def rref(matrix, num_rows, num_columns):
    
    # starts with row 0 as the pivot row
    current_row = 0

    # looks at numbers in each column to find the pivot variable
    for current_column in range(num_columns):
        if current_row >= num_rows:
            break
            
        # (1) Finds the pivot: first non-zero entry in the column
        # Do this by looking at each column's rows
        pivot_row = None
        # Iterates through the number of rows per the column in the for loop
        for i in range(current_row, num_rows):
            if matrix[i][current_column] != 0:
                pivot_row = i

                # displays the pivot number as red
                #RED = "\033[31m"
                #matrix_dis = matrix
                #matrix_dis[pivot_row][current_column] = RED
                #for _ in matrix_dis:
                #    print(_)

                break
        
        # If there is no pivot in this column, skip to the next column
        if pivot_row is None:
            continue

        # (2) Swaps pivot row into the correct position
        matrix[current_row], matrix[pivot_row] = matrix[pivot_row], matrix[current_row]

        # (3) Divides the pivot row such that the pivot number = 1
        pivot_val = matrix[current_row][current_column]
        for i in range(num_columns):
            matrix[current_row][i] = (matrix[current_row][i]) / pivot_val

        # (4) Make all other entries in this column = 0 through Gaussian Elimination
        for i in range(num_rows):
            if i != current_row:
                # for this current row, make the factor = the value found in the first column of that row
                factor = matrix[i][current_column]
                for j in range(num_columns):
                    # (current row-column value) - factor(pivot row's values)
                    matrix[i][j] = (matrix[i][j]) - (factor * matrix[current_row][j]) 
        
        # prints out this step of gaussian elimination
        time.sleep(1)
        print(f"Step {current_row+1} of Gaussian Elimination: ")
        for _ in matrix:
            print(_)
        time.sleep(1)
        
        # (5) Moves on to the next row to find it's pivot
        current_row += 1

    return matrix

main()
