"""
  File: spiral.py
  Description:

  Student Name: Marissa Shuchart
  Student UT EID: ms87339

  Partner Name: Trinity Thompson
  Partner UT EID: tyt242

  Course Name: CS 313E
  Unique Number: 50165
  Date Created: 08/29/2024
  Date Last Modified: 09/03/2024

 Input: n is an odd integer between 1 and 100
 Output: returns a 2-D list representing a spiral
         if n is even add one to n

def create_spiral(n):
    print("REMOVE THIS PRINT AND ADD YOUR CODE")

 Input: spiral is a 2-D list and n is an integer
 Output: returns an integer that is the sum of the
         numbers adjacent to n in the spiral
         if n is outside the range return 0
def sum_adjacent_numbers(spiral, n):
    print("REMOVE THIS PRINT AND ADD YOUR CODE")
"""

import sys

def create_spiral(dim):
    """Creates a Spiral given a dimension for the spiral dimeter"""

    # Create an empty 2D list
    spiral = [[0] * dim for i in range(dim)]

    # Set starting point for the spiral as center of grid
    col = dim // 2
    row = dim // 2

    # Center is 1
    spiral[col][row] = 1

    # Since already placed 1 in center, next num = 2
    num = 2
    step = 1

    while num <= dim**2:
        for i in range(step):
            ''' Have to make sure it exits the for loop if the number
            is larger than dim**2 because won't go back to read the while
            loop until for loop completes'''
            if num > dim**2:
                break
            row += 1 # Move right
            spiral[col][row] = num
            num += 1
        
        for i in range(step):
            if num > dim**2:
                break
            col += 1 # Move down
            spiral[col][row] = num
            num += 1
    
        # For the pattern of the spiral, the step size increases every 2 directions
        step += 1

        for i in range(step):
            if num > dim**2:
                break
            row -= 1 # Move left
            spiral[col][row] = num
            num += 1

        for i in range(step):
            if num > dim**2:
                break
            col -= 1 # Move up
            spiral[col][row] = num
            num += 1

        step += 1

    return spiral



def sum_sub_grid(grid, val):
    """
    Input: grid a 2-D list containing a spiral of numbers
           val is a number within the range of numbers in
           the grid
    Output:
    sum_sub_grid returns the sum of the numbers (including val)
    surrounding the parameter val in the grid
    if val is out of bounds, returns 0
    """
    for col in range(len(grid)):
        for row in range(len(grid)):
            # Find the x and y "coordinates" of the value given and set as center of summation 
            if grid[col][row] == val:
                summation = 0
                # Want to sum the numbers surrounding; range is exclusive at right end
                for i in range(-1, 2):
                    for j in range(-1, 2):
                        # Make sure not to add numbers surrounding if not within the grid
                        if (0 <= (col + i) < len(grid)) and (0 <= (row + j) < len(grid)):
                            summation += grid[col + i][row + j]
                # Don't include the value in the center in the sum
                summation -= val
                return summation
    return 0



def main():
    """
    A Main Function to read the data from input,
    run the program and print to the standard output.
    """

    # read the dimension of the grid and value from input file
    data = sys.stdin.read().splitlines()
    dim = int(data[0])
    
    # test that dimension is odd
    if dim % 2 == 0:
        dim += 1

    # create a 2-D list representing the spiral
    mat = create_spiral(dim)

    for line in data[1:]:
        try:
            sum_val = int(line)

            # find sum of adjacent terms
            adj_sum = sum_sub_grid(mat, sum_val)

            # print the sum
            print(adj_sum)
        except EOFError:
            break

if __name__ == "__main__":
    main()
