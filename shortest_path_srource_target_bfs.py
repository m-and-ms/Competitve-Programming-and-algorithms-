#bfs shortest path from source to target 

def bfs(src,tgt,adj):
    num_nodes=len(adj)
    
    visted=[False]*num_nodes
    
    dist=[-1]*num_nodes
    queue=[]
    
    visted[src]=True
    queue.append(src)
    dist[src]=0
    
    while(len(queue)):
        parent=queue[0]
        queue.pop(0)
        if(parent==tgt):
            break
        for child in adj[parent]:
            

            if(not visted[child]):

                visted[child]=True
                queue.append(child)
                
                dist[child]=dist[parent]+1


    print("dist",dist)           
    return dist[tgt]          
    
def build_adj(adj,u,v):
    adj[u].append(v)    
    
    
def main():
    num_nodes= 4
    adj=[[]for i in range (num_nodes)]
    
    build_adj(adj,0, 1) #0->1 ->2 
    build_adj(adj,0, 2)  #1->2 
    
    build_adj(adj,1, 2)
    build_adj(adj,2, 0)
    build_adj(adj,2, 3)
    build_adj(adj,3, 3)
    print(bfs(0,2,adj))
    
main()
    
    
