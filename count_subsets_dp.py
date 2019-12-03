#subset sum diviible by k dp 
# have array or numbers size n and we shall find if a given subset of numbers could sum up to s which s %k=0

#arr=[1 ,2 5 ,7] k=4 

def sum_subset(idx,sum_mod,n,k,count):
    

        
    
    
    if(k ==0 or k==1):
        return n 
    if(n==0):
        return 0
     
    if(str(idx)+':'+str(sum_mod) in mem.keys()):
#        print(mem)

        
        return mem[str(idx)+':'+str(sum_mod)]
        
    if(sum_mod%k==0 and sum_mod>0 ):
        
        
        count+=1
        print(count)
        
        return count
    
    if(idx==n):
#        print("udxn",count)
        return 0
    return1= sum_subset(idx+1,sum_mod+arr[idx],n,k,count)
    return2=sum_subset(idx+1,sum_mod,n,k,count)
#    sum_subset(idx+1,(sum_mod+arr[i])%k,n,k) #took the item 
    
#    sum_subset(idx+1,sum_mod,n,k) # didnt take it 

    mem[str(idx)+':'+str(sum_mod)]=return1 +return2
    
    return mem[str(idx)+':'+ str(sum_mod)]
    
def main():
    global arr
    global mem 
    mem ={}
    arr=[1,2, 5, 6,3,8]
    k=7 
    
    print(sum_subset(0,0,len(arr),k,0))
main()    
    
    
    
 # repat states   ex 1 +2 +5  or 1 + 2 +6       or   
    
# mem => key idx:sum_mod
    
    
    
    
    

