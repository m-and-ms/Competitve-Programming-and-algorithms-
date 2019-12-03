def decomp(idx,str,text):
    
    if(idx<=0):
        return  str[::-1] #base case
    if(text [idx].isdigit()):
        decomp(idx-1,str,text)
        
    if( text[idx] ==']' ):
        return decomp(idx-1,str,text)
        
    if(text[idx].isalpha()):
        return decomp(idx-1,str+text[idx],text)
        
    if(text[idx]=='[' and text[idx-1].isdigit() and idx-1==0):
        
#        str=int(text[idx-1])*str 
#        print(str)
        
        return decomp(idx-2,int(text[idx-1])*str ,text)

    if(text[idx]=='[' and text[idx-1].isdigit() and idx-1>0):
        
#        str=int(text[idx-1])*str 
#        print(str)
        strsub=int(text[idx-1])*str

        
        return decomp(idx-2,'' ,text)+strsub        
        
    
def main():
    text="3[abc2[ab]]"
    text2="2[ab]2[g]"
    str=''
    strsub=decomp(len(text)-1,str,text)
    print(strsub)

main()    
