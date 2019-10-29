# FLOOD FILL 
#..X.
#.X.X
#..X.       

grid=[['.','.','X','.'],['.','X','.','X'],['.','.','X','.'],['.','X','.','X']]
def is_safe(row,col,grid,visted):
    n=len(grid)
    print(len(grid))
    if(row<n and  col<n or grid[row][col]!='X' or  visted[row][col]==False):
        print(col)
        return True

    return False
def flood_fill(row,col,cnt,grid):
    visted=[len(grid)*[False] for i in range(len(grid))]
    print(visted)
    if(not is_safe(row,col,grid,visted)):
        return False
    visted[row][col]=True    
    flood_fill(row+1,col,cnt+1,grid)
    flood_fill(row,col+1,cnt+1,grid)
    flood_fill(row-1,col,cnt+1,grid)
    flood_fill(row,col-1,cnt+1,grid)
    
        
    return True
    
def pr_cnt(grid)  :
    cnt=0
    flood_fill(0,0,cnt,grid)    
    print (cnt)    
        
    
pr_cnt(grid)    

