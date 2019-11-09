#symetric BST using dfs 
# asemeterical tree should be 
#           1
#        2      2
#    4     3  3    4
# we want to return true if yes
# traverse each node as source in left and right
class node:
    def __init__(self,val):
        self.right=None
        self.left=None
        self.val=val
        
def symetric_tree(src_l,src_r):
    
    if(src_r ==None and src_l==None ):
        return True # if the tree is null or it finshed recursing and return true base case
        
    if(src_r ==None or src_l==None):
        return False
    if(src_l.val!=src_r.val):
        return False
    if(symetric_tree(src_l.left,src_r.right) and symetric_tree(src_l.right,src_r.left)): #cheak for the left.left and right.right
    #check for the left.right and right.left 
        return True
        
      
    return False
def main():
    src_l=node(1)
    src_r=node(1)
    src_l.left=node(2)
    src_r.right=node(2)
    
    src_l.left.left=node(4)
    src_r.right.right=node(4)
    src_l.left.right=node(3)
    src_r.right.left=node(3)    
    print(symetric_tree(src_l,src_r))
    
