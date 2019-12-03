class TrieNode:
    def __init__(self):
        
        self.children=[None]*26
        
        self.end_word=False
        
class Trie:
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
            
            root_node.children[char_idx]=self.create_node()
            
            
            self.insert(root_node.children[char_idx],key,idx+1)
            
    def search(self,root_node,key,idx): #recursive fundtion for searching a trie         
        
        if(root_node.end_word):
            return idx

        
        char_idx=ord(key[idx])-ord('a')
        
        if(not root_node.children[char_idx]):
            
            return -1
            
        i=self.search(root_node.children[char_idx],key,idx+1)    
            
        return i    
            
            
            
    
        
#dict = ["cat", "bat", "rat"]
#"the cattle was rattled by the battery"

def place_in_trie(dict_w,trie_tree):
    for i,item in enumerate(dict_w):
        trie_tree.insert(trie_tree.root,item,0)
    
    
    return


def replace(sentence,dict_w,trie_tree):
    word_tokens = sentence.split() 
    
    for j,token in enumerate(word_tokens) :
        idx=trie_tree.search(trie_tree.root,token,0)
        print(idx)
        
        if(idx!=-1):
            word_tokens[j]=token[:idx+1]
    str_reconstructed=' '.join(word_tokens)    
    
    return str_reconstructed     
            
def main():
            
    dict_w = ["cat", "bat", "rat"]
    sent="the cattle was rattled by the battery"
    trie_tree=Trie()
    place_in_trie(dict_w,trie_tree)
    print(replace(sent,dict_w,trie_tree))
    
    
main()    
        

