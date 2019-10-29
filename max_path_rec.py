#5 1 2
#6 7 8
#1 8 9
#alowed to mive down or right 
grid=[[5, 1, 2],[6, 7 ,8],[1, 8 , 9]]
def is_valid(row,col):
    n=len(grid[0])
    if(row<=n-1 and col <=n-1):
        return True
    return False     
    

def max_path(row,col,grid):
#base base to stop 
    n=len(grid[0])
    if(row==n-1 and col==n-1):
        
        return grid[row][col]
        
    if(not is_valid(row,col)):
        return 0
        #down chocice
    path1=max_path(row+1,col,grid)
        #right choice 
    path2=max_path(row,col+1,grid)
        
    return grid[row][col]+max(path1,path2) 
        
    
print(max_path(0,0,grid))
