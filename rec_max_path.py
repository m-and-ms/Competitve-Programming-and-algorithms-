from collections import defaultdict
# tree           1

#        3     4        5
#      7 2 6  8 9 10  11  12

def max_path_dfs(src,visted,tree,max_path,path):
    path+=src
    visted[src]=True

    if(not tree[src]):
        return path
    

    for childs in tree[src]:
        
        if(not visted[childs]):
            p=max_path_dfs(childs,visted,tree,max_path,path)
            
            max_path=max(max_path,p)    
    
    return max_path
        
        
        
def add_edge(u,v):
    tree[u].append(v)
def main():
    
    
    
    num_nodes=11
    global tree 
    tree =defaultdict(list)
    visted=[False]*(18)
    
    add_edge(1,3)
     
    add_edge(1,4)
    add_edge(1,5)
    add_edge(3,17)
    add_edge(3,2)
    add_edge(3,6)
    add_edge(4,8)
    add_edge(4,9)
    add_edge(4,10)
    add_edge(5,11)
    add_edge(5,12)
    
    print(max_path_dfs(1,visted,tree,0,0))    
        
main()    
