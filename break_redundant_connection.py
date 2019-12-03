from collections import defaultdict


#redundant connections  leet code problem 


#input=[[1,2],[2,3],[3,4],[1,4],[1,5]] 5->1->2
#                                        |   |
#                                        4<-3 we will need to cut the edge betweem  1,2,or 2,3 or3,4 4,1 to return a tree that has no cycles  
#if there is multiple solutions like above (if there are multiple answers, return the answer that occurs last in the given 2D-array in input )


def break_cycle(src,parent,visted,adj,cycle):
    if(visted[src]):
        if(src!=parent):
            cycle.append({parent,src})
            return

    visted[src]=True
    for child in adj[src]:
        if (not visted[child]):
            break_cycle(child,src,visted,adj,cycle)


            
        
def add_edge(u,v,adj):
    adj[u].append(v)
    adj[v].append(u)


    
def main():
    cycle=[]
    
    V=5

    adj=[[] for i in range(V)]

    add_edge(1,2,adj)
    add_edge(2,3,adj)
    add_edge(3,4,adj)
    add_edge(4,1,adj)
    add_edge(5,1,adj)

    visted=[False]*(len(adj)+1)
    for src in range(len(adj)):
        if(not visted[src]):
            break_cycle(src,-1,visted,adj,cycle)
    print(cycle)
    
main()    
            

