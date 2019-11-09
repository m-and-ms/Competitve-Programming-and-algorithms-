#max depth binary tree \\

# dfs recursive approach 
class node:
    def __init__(self,val):
        self.right=None
        self.left=None
        self.val=val

def max_depth(src,count ):
    if(not src):
        return count #base case 
    left_depth=max_depth(src.left,count+1) 
    right_depth=max_depth(src.right,count+1)
        
    return max(left_depth,right_depth)
    
    
def main():
    src=node(1)
 
    src.left=node(2)
    src.right=node(2)
    
    src.left.left=node(4)
    src.right.right=node(4)
    src.left.right=node(3)
    src.right.left=node(3) 
    src.right.right.right=node(5) 
    print(max_depth(src,0))
main()   
