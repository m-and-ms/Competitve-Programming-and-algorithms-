def rec_dfs(adj,src,visted):
    print(src)
    visted[src]=True
    for child in adj[src]:
        if(not visted[child]):
            
            rec_dfs(adj,child,visted)# run the dfs on each child as its the sourse node of smaller branch
            
def addEdge(adj,V,u,w): 
    
    adj[u].append(w)            
            
            
def main():
    
    V=4
    visted=V*[False]
    adj=[[] for i in range(V)]
    addEdge(adj,V,0, 1)
    addEdge(adj,V,0, 2)
    addEdge(adj,V,1, 2)
    addEdge(adj,V,2, 0)
    addEdge(adj,V,2, 3)
    addEdge(adj,V,3, 3)

#    addEdge(adj,V,3, 3)
    print(adj)
    rec_dfs(adj,2,visted)            
    
main()    
