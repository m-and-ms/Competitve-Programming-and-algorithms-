# Hello World program in Python
    
print "Hello World!\n"

import string 
import re

str="may"

print(list(str))


def solve(strA,k):
    
    strA=re.sub(r'-','',strA)
    strA=re.sub(r'/','',strA)

    print(strA)
    len_str=len(strA)
    str_build=[]
    str_temp=""
    strA=list(strA)
    while(strA):
        
        if(len(strA)>=k):
            for i in range(k):
                str_temp+=strA.pop(-1)
            str_temp=str_temp[::-1]
            print(str_temp)
            str_build.append(str_temp.upper()+'-')
            
            str_temp=""

        else:
            for i in range(len(strA)):
                str_temp+=strA.pop(-1)
            str_temp=str_temp[::-1]
            str_build.append(str_temp.upper()+'-')
                
                
    str_build.reverse()
    return ''.join(str_build)[:-1]
    
    
print(solve("2-5g-3-J",2))    

