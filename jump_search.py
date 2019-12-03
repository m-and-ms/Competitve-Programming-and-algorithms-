import numpy as np
def linear_search(val,arr,start,end):
    for i in range(start,end):
        
        if(arr[i]==val):
            return i
            
    return -1

def jump_search(arr,val):
    
    n=len(arr)
    
    jump_sz=int(np.sqrt(n))
    start=0
    
    if(start<len(arr)):    
        while(arr[start] <val):
            
        
            start+=jump_sz
        prev=start-jump_sz
        
    return(linear_search(val,arr,prev,start))
        
def main():
    arr=[ 0, 1, 1, 2, 3, 5, 8, 13, 21, 
    34, 55, 89, 144, 233, 377, 610 ]
    
    print(jump_search(arr,55))
        
        
main()    
    
    
