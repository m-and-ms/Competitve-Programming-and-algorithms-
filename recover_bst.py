#recover binary search tree 2 swapped elements by mistake needs to be recovered  ->the idea is that the in order (dfs ) of bst 
# will form a sorted arrayb with and in this case this array wil either has two anomlies or 1 anomnly 
# first , middle and last are three pointerns to keep track of anomlies
#prev keeps track of previos element in traversal 

class node :
    def __init__(self,val):
        self.val=val
        self.right=None
        self.left=None
        
    
def recover_bst(src,prev,first,middle,last):
    if(not src):
        return 
    #base case end of traversal 
    recover_bst(src.left,prev,first,middle,last)#reach left most point of the bottom of the tree 
    
    if(prev):
        if(src.val<prev.val):
            #anomly detected 
            if(not first ):
                first=prev
                middle=src
            else :
                #second anomly detected 
                last=src
    prev=src
    recover_bst(src.right,prev,first,middle,last)
    
    #when recusing on the right sub tree cuz the right branch will act as a child (current src )and the prev will be the mother node 
    
def swap_bst(first,middle ,last):
    
    if(not last):
        temp=first.val
        
        first.val=middle.val
        
        middle.val=temp
    else :
        temp=first.val
        
        first.val=last.val
        
        last.val=temp
def print_inorder(src):
    #prints the traversal after and before recovery prints dwon to top 
    if(not src):
        return
    print_inorder(src.left)
    print("src",src.val)
    print_inorder(src.right)
    
    

def main():
    first,middle,last,prev=node(False),node(False),node(False),node(False) 
    
    src=node(6)
    src.right=node(2)
    src.left=node(10)
    src.right.right=node(12)
    src.right.left=node(7)
    src.left.left=node(1)
    src.left.right=node(3)
    
    print_inorder(src)# before recovery
    
    recover_bst(src,prev,first,middle,last)
    swap_bst(first,middle ,last)
    
    print_inorder(src) #after recovery 
main()    
                
        
