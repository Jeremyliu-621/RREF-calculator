"""

A calculator that turns any nxm matrix into it's RREF form!
Based on our learnings from UofT's First Year Engineering linear algebra course!
Includes pivots and gaussian elimination.

Jeremy Liu
10/29/2025

"""

def main():
    get_matrix()

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
        
        # the list form of the "row_nums" strs are converted to floats, then appended to a list.
        num_list = []
        for num in row_nums:
            num_list.append(float(num))
        # list is then appended to the matrix_list.
        matrix_list.append(num_list)

    print("Your matrix: ")
    for row in matrix_list:
        print(row)

#def rref():

main()