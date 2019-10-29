import string 

import numpy as np 


def display(grid):
    grid_sz=4
    for i in range(grid_sz):
        for j in range(grid_sz):
            print(str(grid[i][j]) + " ", end ="") 
        print("") 

def is_safe(row,col,forbiden,grid):
    grid_sz=grid.shape[0]

    if(row>=0 and col>=0 and col<grid_sz and row<grid_sz and forbiden[row][col]!=0):
        return True
    else:
        return False
def solve_maze(row,col,forbiden,grid):
    grid_sz=grid.shape[0]
    grid[row][col]=1

    if(col==grid_sz-1 and row==grid_sz-1):

       return True
        
    if(is_safe(row+1,col,forbiden,grid)):
        if(solve_maze(row+1,col,forbiden,grid)):
            return True


            
    if(is_safe(row,col+1,forbiden,grid)):
        if(solve_maze(row,col+1,forbiden,grid)):
            return True
            
    else :
        grid[row][col]=0
        return False
    

def main():
    grid=np.zeros((4,4))
    forbiden=[ [1, 0, 0, 0], 
             [1, 1, 0, 1], 
             [0, 1, 0, 0], 
             [1, 1, 1, 1] ] 
                       
                       
    solve_maze(0,0,forbiden,grid)
                       
    display(grid)
        
if __name__ == "__main__":
    main()
        
        
