
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

def bfs(src):
    dist={}
    visted={}
    queue=[]
    
    queue.append(src)
    visted[src]=True
    dist[src]=0
    
    
    
    while len(queue):
        parent=queue.pop(0)
        if(is_balanced(parent)):
            continue 
        
        neighbours=is_adj(parent)
        
    
        for child in neighbours :
            if( visted.get(child) ==None):
                
                
                visted[child]=True
                queue.append(child)
                dist[child]=dist[parent]+1
                
        
    return dist    
    
def main():
    balanced={}
    src="()())()"
    dst=(bfs(src))
    print(dst)
    for key,val in dst.items():
        if(is_balanced(key)):
            
            balanced[key]=val
            
    print(balanced)
    
    print("Iam Top Coder :D ")
    min_edits=min(balanced.items(),key=lambda x:x[1])
    print(min_edits)    
main()    
    
