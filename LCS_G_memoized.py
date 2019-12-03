 #Input: s1 = “ABCDGH”, s2 = “AEDFHR”
#Output: 3                 a_idx        b_idx     
#LCS for input Sequences “AGGTAB” and “GXTXAYB” is “GTAB” of length 4.
 # AGGTAB ,GXTXAYB
 #repeated states 
 
 #mem[str(a_idx)+":"+str(b_idx)]=count
 
 
def LCS(stra,strb,a_idx,b_idx):
    if(mem.get(str(a_idx)+":"+str(b_idx))):
        print(mem[str(a_idx)+":"+str(b_idx)])

        return mem[str(a_idx)+":"+str(b_idx)]
     
    if(a_idx<0 or b_idx<0):
        return 0 
         
    if(stra[a_idx]==strb[b_idx]):
        mem[str(a_idx)+":"+str(b_idx)]=1+LCS(stra,strb,a_idx-1,b_idx-1)
        
        return mem[str(a_idx)+":"+str(b_idx)] #move both counters 
        
    else :# we didnt find a comon letter 
        move1=LCS(stra,strb,a_idx-1,b_idx)
        
        move2=LCS(stra,strb,a_idx,b_idx-1)
        
        mem[str(a_idx)+":"+str(b_idx)]=max(move1,move2)
        return  mem[str(a_idx)+":"+str(b_idx)]
        
def main():    
    global mem
    mem={}
   
    stra="AGGTAB"
    strb="GXTXAYB"
    print(LCS(stra,strb,len(stra)-1,len(strb)-1))

main()            
