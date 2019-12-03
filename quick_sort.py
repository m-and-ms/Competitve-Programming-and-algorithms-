#quick sort implementation


def swap(left,right,arr):
    
    arr[left],arr[right]=arr[right],arr[left]

def partion(arr,left,right ,pivot):
    
    
    while(left<=right):
        
        while(arr[left]<pivot):
            left+=1
            
        while (arr[right]>pivot):
            right-=1
            
        if(left<=right):
            
            swap(left,right,arr)
            
            left+=1
            right-=1
            
            
    return left      # new dividing point that is whenn the left and right meet     
        
    
    
    
def quick_sort(arr,left,right):
    #left and right are 2 pointers
    if(left>=right):
        return # return case 
    
    pivot=arr[int((right+left)/2) ]
    
    #or if pivot = arr[right ] the high partion should end at right-1
    
    partion_index=partion(arr,left,right,pivot)
    
    
    quick_sort(arr,left,partion_index-1)
    quick_sort(arr,partion_index,right)
    
def main():
    arr=[10, 7, 8, 9, 1, 5]
    
    quick_sort(arr,0,len(arr)-1)
    
    print(arr)
    
    
main()    
