# dfs implemntation using stack iterative 
def dfs_iter(adj,src,nodes):
    #adjaceny matrix [[1 2 3]
    #                 [4 5 6]
    #                 [7 8 9]]            
    
    visted=[False]*nodes
    stack=[]
    visted[src]=True
    stack.append(src) # first tracverse the source node 
    while(len(stack)):
        parent=stack.pop()
        print(parent)
        
        for child in adj[parent]:
            if(not visted[child]):
                visted[child]=True
                stack.append(child)
                
            
def addEdge(adj,V,u,w): 
    
    adj[u].append(w)
    
       
def main():
    V=5
    adj=[[] for i in range(V)]
    addEdge(adj,V,1, 0)
    addEdge(adj,V,0, 2)
    addEdge(adj,V,2, 1)
    addEdge(adj,V,0, 3)
    addEdge(adj,V,1, 4)
#    addEdge(adj,V,3, 3)
    print(adj)
    dfs_iter(adj,0,V)
    
    
main()    
