def is_adj(parent):
    
    
    row =parent[0]
    col =parent[1]
    possible_states =[(row ,col+1) ,(row ,col-1) ,(row+1 ,col) ,(row-1 ,col)]
    return possible_states
def isSafe(child ,grid):
    row_i =child[0]
    col_i =child[1]
    if (row_i>=0 and row_i < len(grid) and col_i>=0 and col_i <len(grid[0]) and grid[row_i][col_i] !=2) :
        return True
    return False    
    


def bfs(src ,grid):
    
    q=[]
    visited=[[0 for j in range(len(grid[0]))] for i in range(len(grid))]
    dist=[[-1 for j in range(len(grid[0]))] for i in range(len(grid))]
    
    visited[src[0]][src[1]]=1
    
    q.append(src) 
    dist[src[0]][src[1]]=0    
    while (len(q)):
        
        parent =q.pop(0)
        if grid[parent[0]][parent[1]] ==1 :
            continue
        
        for state in is_adj(parent) :
            
            if (isSafe(state ,grid) and not visited[state[0]][state[1]] ):
                
                visited[state[0]][state[1]] =1
                q.append(state)
                
                dist[state[0]][state[1]]=dist[parent[0]][parent[1]]+1
                
                
    return dist
def find_zeros(grid):
    zeros=[]
    
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if (grid[i][j]==0):
                zeros.append((i,j))
    return zeros 
def find_ones(grid):
    ones=[]
    
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if (grid[i][j]==1):
                ones.append((i,j))
    return ones     
    
def find_sol( grid)  :
    paths={}
    location_zeros=find_zeros(grid)
    location_ones=find_ones(grid)
 
    for zero in location_zeros :
        distance=bfs(zero,grid)
        tot_dst =calc_total(distance,location_ones)
        
        paths[zero] =tot_dst
    if(not bool(paths)):
        return -1
    
    return min(paths.items(),key=lambda x:x[1])
        
        
def calc_total(dst_array,ones):
    tot_dst=0
    for one in ones :
        x=one[0]
        y=one[1]
        tot_dst +=dst_array[x][y]
    
    return tot_dst
        

def main():
    
    grid =[[1,0,2,0,1],[0,0,0,0,0] ,[0,0,1,0,0]]
    print ( find_sol( grid))
    




if __name__ =="__main__":
    
    
    main()

