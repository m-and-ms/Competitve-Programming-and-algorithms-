def decomp(idx,str,text,stack):
    
    if(idx>len(text)-1):
        
        return str
    if(text[idx]=="]" and idx==len(text)-1):

        if(not len(stack)):
            return str     
        else :
            return str*int(stack.pop(0))
            
    if(text[idx]=="]" and idx<len(text)-1 ):
        repeat=stack.pop(0)
        print(repeat)

        str=str*int(repeat)
        strsub=decomp(idx+1,"",text,stack)
        print("1",strsub)
        print("2",str)

        return str+ strsub        
    if(text[idx].isalpha()):
         return decomp(idx+1,str+text[idx],text,stack)
    if(text[idx].isdigit()):
        stack.append(text[idx])
        print(stack)



        return decomp(idx+1,str,text,stack)
        
    if(text[idx]=="["):

        return decomp(idx+1,str,text,stack)
def main():
    text="3[abc2[ab]]"
    text2="2[ab]2[g]"
    str=''
    stack=[]
    strsub=decomp(0,str,text,stack)
    print(strsub)

main()            
