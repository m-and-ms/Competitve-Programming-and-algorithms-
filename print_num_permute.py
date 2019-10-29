
#gen all possible permutation of numbers fro 0 to n-1 
#0 1 2 3 ->num_array 
# prm_array =[0 2 1 3] -> idx is how much numbers put in the perm array
n=3
num_array=[i for i in  range (n)]
def pri_perm(idx,prm_array,vist):
    if(idx==n):
        print(prm_array)

        
        
        return 
    for num in num_array:
        
        if(not vist[num]):
            vist[num]=True
            prm_array[idx]=num
            
            pri_perm(idx+1,prm_array,vist)
        vist[num] =False 
    

def main():
    vist=n*[False]
    prm_array=n*[0]
    
    
    pri_perm(0,prm_array,vist) #printing permutation of length  n
    
    
    
main()    
            
        
