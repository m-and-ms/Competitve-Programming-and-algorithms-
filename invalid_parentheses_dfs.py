
def is_adj(parent_expression):
    str_adj=[]
    for idx,bracket in enumerate(parent_expression) :
        if(bracket.isalpha()):
            continue
        str_adj.append(parent_expression[:idx]+parent_expression[idx+1:])
    return str_adj


def is_balanced(str):
    stack=[]
    
    for char in str:
        if(char=="("):
            stack.append(char)
            continue #to not continue in the iteration
        if(len(stack)==0):# stack should have the open brackets else false 
            return False
            
        if(char==")") :
            front=stack.pop()
            if(front!="("):
                return False
    if(len(stack)):
        return False #unbalanced open are more than closed beccause stack is not empty
    
    return True

def dfs(src,visted,count,balanced_stk):
    
    
    visted[src]=True
    if(is_balanced(src)):
        balanced_stk[src]=count
        return  
    
    neighbours=is_adj(src)
    
    for child in neighbours :
        if(not visted.get(child)):
            
        
            dfs(child,visted,count+1,balanced_stk)
            
            

        
def get_min(min_val,d,min_edit):
    for k,v in d.items():
        if(v==min_val[1]):
            min_edit.append((k,v))
            

    
    
def main():
    min_edit=[]

    src="()())()"
    balanced_stk={}
    visted={}
    dfs(src,visted,0,balanced_stk)
    print(balanced_stk)
#    min_edit.append(min(balanced_stk.items(),key=lambda x:x[1]))
    print(min_edit)
    get_min(min(balanced_stk.items(),key=lambda x:x[1]),balanced_stk,min_edit)
    
    print(min_edit)
    
main()    
