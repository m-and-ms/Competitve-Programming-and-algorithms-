#symetric BST using BFS
# asemeterical tree should be 
#           1
#        2      2      q=[2,2]
#    4     3  3    4  q=[4 3 2] ->q=[4 3 3 4]
# we want to return true if yes
# traverse all nodes of same level using bfs , uses q to store the values of the same level together compares r_node.right and lnode.left
# compares r_node.left and l_node.right

def symetric_tree_iter(src):
    if(src==None):
        return True
    if(not src.left and not src.right):
        return true # a null tree 
    queue=[]
    queue.append((src,src)) #appended src 2 times
        
    while(len(queue)):
        src_l=queue[0][0]
        src_r=queue[0][1]
        queue.pop(0)



        if(src_l.val!=src_r.val):
            return False
        if (src_l.left and src_r.right):
            
            queue.append((src_l.left,src_r.right))
        
        elif(not src_l.left or not src_r.right):
            return False
        
       
        if(src_l.right and src_r.left):
            queue.append((src_l.right,src_r.left)) 
        elif(src_r.left==None or src_l.right==None ):
            return False        
        
    return True    
            


    
    
    
    
    
    
    
    
    
    
class node:
    def __init__(self,val):
        self.right=None
        self.left=None
        self.val=val
        



def main():
    src=node(1)
 
    src.left=node(2)
    src.right=node(2)
    
    src.left.left=node(4)
    src.right.right=node(4)
    src.left.right=node(3)
    src.right.left=node(3)    
    print(symetric_tree_iter(src))
main()    
    
