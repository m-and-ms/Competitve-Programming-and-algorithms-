from collections import defaultdict

def is_adj(src):
    row=src[0]
    col=src[1]
    
    adj_list=[(row+2,col+1),(row+1,col+2),(row-1,col+2),(row-2,col+1),(row-2,col-1),(row-1,col-2),(row+1,col-2),(row+2,col-1)]
    return adj_list
def is_valid(src,n):
    
    
    rw=src[0]
    
    col=src[1]
    
    if(rw<n and  col<n and rw>0 and col >0):
        return True
        
    return  False    
    

def knight_tour(src,visted,n):
    visted[src[0]][src[1]]=True
    if(src[0]==n-1 and src[1]==n-1):
        
        return True
    

    
    #src is the current state row,col 
    
    

        
    adj_states=is_adj(src)   
    for state in adj_states:
        print(state)
        
        if(is_valid(state,n) and not visted[state[0]][state[1]]):
            
            if(knight_tour(state,visted,n)):
                
                
                return True
                
            else :
                
                visted[src[0]][src[1]]   =False
            
    return False     
            
            
def main():
    
    
    n=8
    visted=[[False for i in range(n)] for i in range(n)]
    
    src=(0,0)
    
    print(knight_tour(src,visted,n))
    print(visted)
    
                
            
main()         	
