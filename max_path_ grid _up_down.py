#max_path_ grid up down approach
#1 4 7
#2 8 1
#3 6 9
#alowed to mive down or right 
global grid
grid =[[  1 ,4  ,7 ],[2 ,8  ,1]  ,[3  ,6  ,9]]
def is_valid(row,col):
    n=len(grid[0])
    if(row<n and col <n):
        return True
    return False     

def max_grid(row,col,path,max_path_):
    if(row ==len(grid)-1 and col ==len(grid)-1):
        return path+grid[row][col]
        
        
    else :
        if(is_valid(row,col)):
            
            
            pdown=max_grid(row+1,col,path+grid[row][col],max_path_)
        
            pright=max_grid(row,col+1,path+grid[row][col],max_path_)
        
            max_path_=max(pdown,pright)    
    return max_path_    
    
    
print(max_grid(0,0,0,0))    
