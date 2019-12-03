class TrieNode:
    def __init__(self):
        
        self.children=[None]*26
        
        self.end_word=False
        
def Trie :
    def __init__(self):
        self.root=self.create_node()
        
    
    
    
    def create_node(self):
        
        return TrieNode()
        
        
    def insert(self,root_node,key,idx): #recursive implementation eg inset "card" in trie 
        if(idx==len(key)-1):
            
            root_node.end_word=True
            
            return 
        
        
        
        char_idx=ord(key[idx])-ord('a')
        
        if(not root_node.children[char_idx]):
            
             root_node.children[char_idx]=create_node()
            
            
            insert(self,root_node.children[char_idx],key,idx+1)
            
    def search(self,root_node,key,idx): #recursive fundtion for searching a trie         
        if(idx==len(key)-1):
            if(root_node.end_word):
                return True
            return False
        
        char_idx=ord(key[idx])-ord('a')
        
        if(not root_node.children[char_idx]):
            
            return False
            
        search(root_node.children[char_idx],key,idx+1)    
            
            
            
            
            
    
        
        
        
        
        
