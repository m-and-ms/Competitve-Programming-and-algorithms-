#genrate binary seq of length n
#           0       1
#          00 01    10 11  n=2
# 000 001 010 011   100 101 110 111 n=3

def gen_binary(n,strb,length):
    print(strb) # print all combinations n=1,2,3
    if(length==n):
        print(strb) # print all combinations n=3

        return strb
    gen_binary(n,strb+"0",length+1)
    gen_binary(n,strb+"1",length+1)
    
    
gen_binary(3,"",0)    
    
    

