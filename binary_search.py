def binary_search(val,L,R,arr):
    
    
    if(R-L<=0):
        return -1 # base case right < left 
        
    mid=int(L+(R-L)/2)  
    
    if(arr[mid]==val):
        return mid 
        
    if(val >arr[mid]):
        
        return(binary_search(val,mid+1,R,arr))
        
    if(val<arr[mid]):
        
        return(binary_search (val,l,mid-1))
        
    
    
def main():
    arr = [ 2, 3, 4, 10, 40 ] 
    x = 10
    
    print(binary_search(x,0,len(arr)-1,arr))
        
    
main()        
