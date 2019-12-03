 #Input: s1 = “ABCDGH”, s2 = “AEDFHR”
#Output: 3                 a_idx        b_idx     
#LCS for input Sequences “AGGTAB” and “GXTXAYB” is “GTAB” of length 4.
 # AGGTAB ,GXTXAYB
 #repeated states 
 
 #mem[str(a_idx)+":"+str(b_idx)]=count
 
def LST(stra,strb,a_idx,b_idx,count,c1):
    if(mem.get(str(a_idx)+":"+str(b_idx))):
        print(mem[str(a_idx)+":"+str(b_idx)])
        return(mem[str(a_idx)+":"+str(b_idx)])
     
    if(a_idx>=len(stra) or b_idx>=len(strb)):
         
        return  count
        
    if(strb[b_idx:].find(stra[a_idx])!=-1):
        print("hello")
        b_idx=strb[b_idx:].find(stra[a_idx])
        
        c1=LST(stra,strb,a_idx+1,b_idx+1,count+1,c1)
        
        mem[str(a_idx)+":"+str(b_idx)]=c1
        
    else:
        
        c1=LST(stra,strb,a_idx+1,b_idx,count,c1)
        mem[str(a_idx)+":"+str(b_idx)]=c1
    return mem[str(a_idx)+":"+str(b_idx)]    
def find_all(stra,strb):
    max_cnt=0
    b_idx=0
    for start in range(len(stra)):
        cnt=LST(stra,strb,start,b_idx,0,0)
        max_cnt=max(cnt,max_cnt)
        mem[str(start)+":"+str(b_idx)]=max_cnt
    return mem[str(start)+":"+str(b_idx)]
        
        
    
def main():    
    global mem
    mem={}
   
    stra="AGGTAB"
    strb="GXTXAYB"
    print(find_all(stra,strb))
    print(mem)

main()    
     
     
