
# n C r ex choose groups of 3 out 4 children
#[A B C D] (elements)   ->ABC ->ABD ->ADC ->BCD 
#A take it [A] or leave it [""]
#idx is a conter to keep track of current element either to take or leave #
# curr_len measures the number of appended elements in the comb str we want to collect a comb _arr of length r 

def gen_comb(elements,n,r,comb,idx_e,curr_len):
    if(curr_len==r):
        print(comb)
        return
    if(idx_e==n):
        return # we reached the end of the elemnet list and we didnt have yet a comb arr of length r 
    
    gen_comb(elements,n,r,comb+elements[idx_e],idx_e+1,curr_len+1) # we took the elememnt 
    
    
    # we didnt take the elememnt 
    gen_comb(elements,n,r,comb,idx_e+1,curr_len)
    
    
def main():
    elements =["A" ,"B","C","D"]
    n=len(elements)
    r=3
    gen_comb(elements,n,r,"",0,0)
    
main()    
    
