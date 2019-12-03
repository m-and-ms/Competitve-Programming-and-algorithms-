def merge(arr,Left_arr,Right_arr):
    l_idx,r_idx,k=0,0,0
    
    
    while(l_idx<len(Left_arr) and r_idx<len(Right_arr)): # if bigger would stop 
        print("hello1")
        if(Left_arr[l_idx]<Right_arr[r_idx]):
            arr[k]=Left_arr[l_idx]
            print("hello2")
            l_idx+=1
        else :
            print("hello3")

            arr[k]=Right_arr[r_idx]
                
            r_idx+=1
        k+=1
    

    while(l_idx<len(Left_arr)):
        arr[k]=Left_arr[l_idx]
        
        l_idx+=1
        k+=1
    while  (r_idx<len(Right_arr)):
        arr[k]=Right_arr[r_idx]
                
        r_idx+=1
        k+=1


def merge_sort(arr):

    
    
    #get mid element 
    if(len(arr)>1):
        mid=int(len(arr)/2)
    
        print("arr",arr)
        L=arr[:mid]
        R=arr[mid:]
        merge_sort(L)
        
        merge_sort(R)
    
        merge(arr,L,R)
        
    return
    
def main():
    arr=[12, 11, 13, 5, 6, 7]
    merge_sort(arr)
    print(arr)
    
main()    
    
    
