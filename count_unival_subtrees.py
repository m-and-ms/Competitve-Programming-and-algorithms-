#Input: root of below tree
 #             5
 #            / \
 #          1   5
 #          / \   \
  #        5   5   5
#Output: 4
#There are 4 subtrees with single values.
def is_leaf(src):
    if(not src.left and not src.right):
        return True
    return False
    
    
def count_unival(src,cont,cl,cr):
    if(src==None):
        return 0
    
    
    if(is_leaf(src)):
        
        return cont
    
    if(src.right and src.left and src.right.val ==src.left.val==src.val): # 2 childeren exist
        
            
        cl=count_unival(src.left,cont+1,cl,cr)
        cr=count_unival(src.right,cont+1,cl,cr)
            

       
            
    elif(src.left and not src.right and src.left.val==src.val):
        cl=count_unival(src.left,cont+1,cl,cr)

    elif(src.right and not src.left and src.right.val==src.val) :
        
        cr=count_unival(src.right,cont+1,cl,cr)
        
    else:
        cl=count_unival(src.left,cont,cl,cr)
        cr=count_unival(src.right,cont,cl,cr)
    return cr+cl   
class Node: 
     
    def __init__(self ,val): 
        self.val = val 
        self.left = None 
        self.right = None        

        
def main():
    root = Node(5) 
    root.left = Node(4) 
    root.right = Node(5) 
    root.left.left = Node(4) 
    root.left.right = Node(4) 
    root.right.right = Node(5) 
    print(count_unival(root,0,0,0)) 
    
main()        
        
    
    
