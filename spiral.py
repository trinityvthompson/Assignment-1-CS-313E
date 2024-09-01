"""
  File: spiral.py
  Description:

  Student Name: Marissa Shuchart
  Student UT EID: ms87339

  Partner Name: Trinity Thompson
  Partner UT EID: tyt242

  Course Name: CS 313E
  Unique Number: 
  Date Created: 
  Date Last Modified:

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

import math

def create_spiral(dim):
    """Creates a Spiral given a dimension for the spiral dimeter"""

    spiral = [[0] * dim for i in range(dim)]

    # Set starting point for the spiral as center of grid
    x = dim // 2
    y = dim // 2

    # Center is 1
    spiral[x][y] = 1

    num = 2
    step = 1

    while num <= dim**2: 
        for i in range(step):
            y += 1 # Move right 
            spiral[x][y] = num
            num += 1
        
        for i in range(step):
            x += 1 # Move down
            spiral[x][y] = num
            num += 1
    
        step += 1

        for i in range(step):
            y -= 1 # Move left
            spiral[x][y] = num
            num += 1

        for i in range(step):
            x -= 1 # Move up 
            spiral[x][y] = num
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
    sum = 0
    for x in range(len(grid)):
        for y in range(len(grid)):
            if grid[x][y] == val:
                for i in range(-1, 2):
                    for j in range(-1, 2):
                        sum += grid[x + i][y + j]
                sum -= val
                return sum
                # sum = (grid[x][y-1]) + (grid[x+1][y]) + (grid[x-1][y]) + (grid[x][y+1]) 
            # else:
            #     return 0





def main():
    """
    A Main Function to read the data from input,
    run the program and print to the standard output.
    """

    # read the dimension of the grid and value from input file
    dim = int(input())

    # test that dimension is odd
    if dim % 2 == 0:
        dim += 1

    # create a 2-D list representing the spiral
    mat = create_spiral(dim)

    while True:
        try:
            sum_val = int(input())

            # find sum of adjacent terms
            adj_sum = sum_sub_grid(mat, sum_val)

            # print the sum
            print(adj_sum)
        except EOFError:
            break


if __name__ == "__main__":
    main()

  
