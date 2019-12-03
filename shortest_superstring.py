from collections import defaultdict
#["catg","ctaagt","gcta","ttca","atgcatc"]
#out "gctaagttcatgcatc"
#ctaagt","gcta",
def get_common(parent,child,j,weight,comon):
    min_len=min(len(parent),len(child))
    if(j==len(child)):
        weight=len(child)
        return (weight,comon)
    if(child.find(parent[j:])==0):
        comon+=(parent[j:])
        weight= len(child)-len(comon)
        return (weight,comon)
        
        
    else:
        w=get_common(parent,child,j+1,weight,comon)
        
    return w    
   


def add_child(src,child):
    
    comon=get_common(src,child,0,0,"")
    
    wt=comon[0]
    com_str=comon[1]
    
    summed_str=src+child.strip(com_str)
    return (wt,summed_str)
    
def is_adj(src,str_list):
    adj={}
    adj_l=[]
    if(src in str_list):
        
        str_list.remove(src)
    for child in str_list :
        print(src,child)
        summed_str=add_child(src,child)
        adj_l.append((summed_str[1],summed_str[0]))
    adj[src]=adj_l
#        adj.append()
            
    return adj 
    
def shortest_path(src,str_list):
    pq=[]
    dist=defaultdict(lambda: 10^6)
    
    dist[src]=0
    pq.append((src,0))
    
    while(len(pq)):
        sorted(pq, key = lambda x: x[1]) 
        u=pq.pop(0)[0]
        adj=is_adj(u,str_list)
#        print("adj",adj)
        for child in adj[u]:
#            print("child",child)
            
            v=child[0]
            
            wt_child=child[1]
#            print("wt",wt_child)
            
            if(dist[v]>dist[u]+wt_child):
                dist[v]=dist[u]+wt_child
                
                pq.append((v,dist[v]))
            
    return dist        
            
def main():
    str_list=["catg","ctaagt","gcta","ttca","atgcatc"]
    
    src="gcta"
    dst=shortest_path(src,str_list)
    print(dst)


    

'''
   
def main():
    parent="gcta"
    
    child="ctaagt"
    
    weight=0
    j=1
    comon=""
    
    w=get_common(parent,child,0,weight,comon)
    print(w)

'''
    
main()    
from collections import defaultdict
#["catg","ctaagt","gcta","ttca","atgcatc"]
#out "gctaagttcatgcatc"
#ctaagt","gcta",
def get_common(parent,child,j,weight,comon):
    min_len=min(len(parent),len(child))
    if(j==len(child)):
        weight=len(child)
        return (weight,comon)
    if(child.find(parent[j:])==0):
        print (j)
        comon+=(parent[j:])
        print(comon)
        weight= len(child)-len(comon)
        return (weight,comon)
        
        
    else:
        w=get_common(parent,child,j+1,weight,comon)
        
    return w    
   


def add_child(src,child):
    
    comon=get_common(src,child,0,0,"")
    
    wt=comon[0]
    com_str=comon[1]
    
    summed_str=src+child.strip(com_str)
    return (wt,com_str)
    
def is_adj(src,str_list):
    adj=[]
    str_list.remove(src)
    for child in str_list :
        adj.append(add_child(src,child))
            
    return adj 
    
def shortest_path(src,str_list):
    pq=[]
    dist=defaultdict(lambda: 10^6)
    
    dist[src]=0
    pq.append((src,0))
    
    while(len(pq)):
        u=pq.pop(0)[0]
        adj=is_adj(src,str_list)
        print(adj)
        for child in adj[u]:
            
            v=child[0]
            
            wt_child=child[1]
            
            if(dist[v]>dist[u]+wt_child):
                dist[v]=dist[u]+wt_child
                
                pq.append((v,dist[v]))
            
    return dist        
            
def main():
    str_list=["catg","ctaagt","gcta","ttca","atgcatc"]
    
    src="gcta"
    dst=shortest_path(src,str_list)
    print(dst)


    

'''
   
def main():
    parent="gcta"
    
    child="ctaagt"
    
    weight=0
    j=1
    comon=""
    
    w=get_common(parent,child,0,weight,comon)
    print(w)

'''
    
main()    

