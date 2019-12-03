#                                                          0

#diameter of n-aray tree using bfs   let tree is       1            2 
#                                                   2  3   4      4 7  6     d=7 is between 5 and 5 leaves 
#                                                          5      7   
#                                                                 5
from collections import defaultdict
def bfs_diamter(src,num,adj):
    
    queue=[]
    
    visted=[False]*num
    dist=[-1]*num
    
    queue.append(src)
    
    visted[src]=True
    dist[src]=0
    while(len(queue)):
         
         
        parent=queue.pop(0)
         
        for child in adj[parent]:
            if(not visted[child] ):
                 
                visted[child]=True
                queue.append(child)
                 
                dist[child]=dist[parent]+1
    big = max(dist)
    print(dist)
            
    return((big,dist.index(big)))                
                 
def build_adj(adj,u,v):
    adj[u].append(v)    
    
    
def main():
    num_nodes= 7
    adj=defaultdict(list)
    
    build_adj(adj,1, 2) #        1
    build_adj(adj,1, 3) #  2       3     6    
    #                    4  1  5   1     1
    build_adj(adj,1, 6)# 2    2       
    build_adj(adj,2, 4)#
    build_adj(adj,2, 1)
    build_adj(adj,3, 1)
    build_adj(adj,2, 5)#
    
    
    
    
    build_adj(adj,4, 2)
    build_adj(adj,5, 2)
    build_adj(adj,6, 1)
    max_points=get_diameter(adj,1,num_nodes)
    

def get_diameter(adj,src,num_nodes):
    
    max_point=bfs_diamter(1,num_nodes,adj)
    print(max_point)
    far_most=bfs_diamter(max_point[1],num_nodes,adj)
    
    total_dst=far_most[0]
    print(total_dst)

        
     
     

    
    

    
main()    
    
    
    
    
    
    
