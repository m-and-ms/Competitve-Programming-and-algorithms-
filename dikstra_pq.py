# Hello World program in Python
import numpy as np 
from collections import defaultdict
import string 
import math
inft = 10*6

def build_adj(adj,u,v,wt):
    adj[v].append((u,wt))
    adj[u].append((v,wt))

    
def shortest_path(source,V,adj):
    
    pq=[]
   
    dist=[inft]*V
    
    dist[source]=0
    
    pq.append((source,0))
    
    while(len(pq)):
        
        sorted(pq, key = lambda x: x[1]) 
        
        u=pq[0][0]
        pq.pop(0)
        for child in adj[u]:
            v=child[0]
            wt_child=child[1]
            if (dist[v] >dist[u]+wt_child):
                dist[v]=dist[u]+wt_child
                pq.append((v,dist[v]))
                
    
    for i in range(V):
        print("vertex %s dist %s" % (i, dist[i]))

    
    
def  main():
    V=9
    adj= defaultdict(list)     
    build_adj(adj,0, 1, 4); 
    build_adj(adj,0, 7, 8); 
    build_adj(adj,1, 2, 8); 
    build_adj(adj,1, 7, 11); 
    build_adj(adj,2, 3, 7); 
    build_adj(adj,2, 8, 2); 
    build_adj(adj,2, 5, 4); 
    build_adj(adj,3, 4, 9); 
    build_adj(adj,3, 5, 14); 
    build_adj(adj,4, 5, 10); 
    build_adj(adj,5, 6, 2); 
    build_adj(adj,6, 7, 1); 
    build_adj(adj,6, 8, 6); 
    build_adj(adj,7, 8, 7); 
    shortest_path(0,V,adj)    
        
        
main()
    
    
    
    
