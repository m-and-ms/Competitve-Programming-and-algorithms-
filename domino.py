# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
from collections import Counter

def get_freq(A,B):
    freq_A=Counter(A)
    freq_B=Counter(B)
    max_B_key=max(freq_B.iteritems(), key=operator.itemgetter(1))[0]
    max_A_key=max(freq_A.iteritems(), key=operator.itemgetter(1))[0]
    max_B_val=max(freq_B.iteritems(), key=operator.itemgetter(1))[1]
    max_A_val=max(freq_A.iteritems(), key=operator.itemgetter(1))[1]
    if(max_B_val>max_A_val):
        return (max_B_val,max_B_key)
    else:
        return(max_A_val,max_A_key)

def solution(A, B):
    # write your code in Python 3.6
    pass
    rotations=0
    mx_repeated=0
    flag=1
    global_min=100000
    dict_A={}
    dict_B={}
    len_a=len(A)
    len_b=len(B)
    if(len_a!=len_b):
        return -1
    freq=[0]*7 #values 1 till 6

    for i in range(len_a):
        if(A[i]==B[i]):
            freq[A[i]]+=1  

        else:
            freq[A[i]]+=1
            
            freq[B[i]]+=1
        
    for i in range(1,len(freq)):
        if(len_a ==freq[i]):
            mx_repeated=i
           
            flag=0
            break 
       
    if( flag==1):
        return -1 #no solution 
        
        
        
    else :
        cont_repeat=0
        similar_val=0
        
        
        for i in range(len_a):
            if(A[i]==B[i]):
                similar_val+=1
                
            else:
                if(A[i]==mx_repeated):
                    
                    cont_repeat+=1
        if(global_min>min(cont_repeat,len_a-similar_val-cont_repeat)):
            global_min=min(cont_repeat,len_a-similar_val-cont_repeat)                
                    
        return (global_min)
