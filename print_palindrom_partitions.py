#generate all palindrom partitions 

# nitin -> n i t i n and n iti n 
#geeks -> g e e k s and g ee k s 

def is_pal(pal_str):

    i,j=0,len(pal_str)-1
    while(pal_str[i]==pal_str[j]):
    
       
        if(i<=j and i<len(pal_str) and j>0):
        
        
            i+=1
            j-=1
        else:    
            return True
    else:
        return False
        
        
def pal_part(pal_str,start,part ,pals):
    
    if(start>len(pal_str)):
        
        return
    
    if( len(part) and is_pal(part)):
        pals.append(part)
        
        
    for idx in range(start,len(pal_str)):
        pal_part(pal_str,idx+1,part+pal_str[idx],pals)
        
        
def main():
    pal_str="nitin"
    pals=[]
    pal_part(pal_str,0,"" ,pals)
    print(pals)

     
main()        
        
