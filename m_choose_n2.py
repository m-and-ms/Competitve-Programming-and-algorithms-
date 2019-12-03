#say we have six ppl to be seated in 4 chairs


def m_choose_n(pos,idx,visted,str_comb,n,m):
    if(len(str_comb)==n):
        
        print(str_comb)

        return    
    
    if(pos==n):

        return
    
    


        
    
    while (idx <m):

        
        if(not visted[idx]):
            
            visted[idx]=True
            m_choose_n(pos+1,idx,visted,str_comb+str(idx),n,m)
            visted[idx]=False
            
            m_choose_n(pos+1,idx,visted,str_comb,n,m)
            

        idx+=1    
    return         
            
def main():
    m=6
    n=4
    
    visted=[False]*m
    str_comb=""
    m_choose_n(0,0,visted,str_comb,n,m)
            
main()
    
