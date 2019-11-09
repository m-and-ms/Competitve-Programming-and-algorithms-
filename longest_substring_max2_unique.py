#eceabf -> ece max_len 3
#abccfe -> bcc ,ccf  max_len 3

#longest sub string 
# max 2 unique chracters 

def long_sub(stri):
    visted =256*[0]# 256 chrcahters and all symbolls 
    start,end,unique,max_len=0,0,0,0
    while(end<len(stri)): # while loop that traverses the string 
        if( visted[ord(stri[end])]==0):
            
            if(unique<2):
                visted[ord(stri[end])]+=1
                unique+=1
            else:    
                visted[ord(stri[start])]-=1 #get rid of the first letter and move the counter 
                if(visted[ord(stri[start])]==0):
                    unique-=1 # was a single charcter and shall be removed from unique freq =1
                max_len=max(max_len,end-start) #return the max length of current solution 
                start+=1    # leave the first old chatchter 
                end-=1 # to traverse the last chachter that was traversed but un visted 
        end+=1                
    return max_len                
            
            
def main():
    stri="eceabf"
    stri2="abccfe"
    
    print(long_sub(stri))
    print(long_sub(stri2))
    
    
main()    
