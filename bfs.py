import numpy as np 
from collections import defaultdict
import string 
import math

def build_adj(adj,v,u):
    adj[v].append(u)
    

def BFS(adj,source,V):
    visted=[False]*V
    
    queue=[]
    
    
    visted[source]=True
    queue.append(source)
    
    while(len(queue)):
        
        s=queue[0]#fornt of queue the pop
        print("source",s)
        queue.pop(0)
        
        for childs in  adj[s]:
            print("childs",childs)
            if (visted[childs]==False):
                visted[childs]=True
                
                
                queue.append(childs)
                
                
def main ():
    adj=defaultdict(list)
    V=4
    build_adj(adj,0, 1)
    build_adj(adj,0, 2)
    build_adj(adj,1, 2)
    build_adj(adj,2, 0)
    build_adj(adj,2, 3)
    build_adj(adj,3, 3)
    
    BFS(adj,0,4)
    
    
main()    
    
    
