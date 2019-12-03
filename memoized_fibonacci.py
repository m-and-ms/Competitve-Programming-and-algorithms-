# fibonaci memoized top down approach 

def fib(n):
    print("1",ret[n])
    if(n==0 or n==1):
        return n
    if(ret[n]!=-1):
        print("2",ret[n])
        
        return ret[n]
        
    ret[n]=fib(n-1)+fib(n-2)    
    
    return ret[n]
    
    
    
def main():
    global ret
    ret=[-1]*100
    
    print(fib(5))
main()    
