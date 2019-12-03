################## trie implementatiom



class TrieNode:
    def __init__(self):
        
        self.children=[None]*26
        self.endWord=False



class trieTree:
    def __init__(self):
        
        self.theRoot=self.createNode()
          
    def createNode(self):
        
        return TrieNode()
        
    def Insert(self,key):
        
        nxtPtr=self.theRoot
        for char in key :
            idx_char= ord(char)-ord('a')
            if not nxtPtr.children[idx_char]:
                charnode =self.createNode()
                nxtPtr.children[idx_char] =charnode
            nxtPtr =nxtPtr.children[idx_char]
        
        nxtPtr.endWord =True
    
    
    
    def search(self,key):
        nxtPtr=self.theRoot
        for char in key :
            idx_char= ord(char)-ord('a')
            if not nxtPtr.children[idx_char]:
                return False
            else :
                nxtPtr=nxtPtr.children[idx_char]
            
            
        if (nxtPtr !=None and nxtPtr.endWord ) :
            return True
                
        else :
            return False
            
            
            
            
        def remove_nodes(self,src,key,idx,parent_list):
            
            if (not src):
                return None
            
            if (idx==len(key)-1):  ######check end of the word , unique last node or prefix end 
                if (src.endWord) :
                    src.endWord=False
                     
                if not any(src.children):
                    parent_list.remove(src)
                    src=None
                    
            return src ######## node we end with   
            
            char_idx =ord(key[idx])-ord('a')
            src.children[char_idx]=remove_nodes(src.children[char_idx] ,key ,idx+1,src.children) #removes current node 

            
            #the root would be remenaing 
            
            
            if(not any(src.children) and not src.endWord  ):
                
                parent_list.remove(src)
                
                src=None
    return src            
                
            
