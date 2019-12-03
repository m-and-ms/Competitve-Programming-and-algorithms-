#zealaez -> zea  l  aez  ->aezlzea orignaly odd  min 2
#zeez ->ze ez ->ezze orignally even but no plaindrome cuts  min 1
# zaaz   zaaz ->  ->za azzaaz ->                  aazzaazza                  2 even palindromic cuts  orignalyy even min 1
# asaasa -> asa asa 2 odd palindromic cuts  2 cuts min as aa sa ->   saaaas orignally even min 2
#nolon --> no | l | on --> on | l | no --> onlno
#toottoot --> to | ottoot --> ottoot | to --> ottootto
#voov
#aaaasaaaa
def is_pal(pal_str):

    i,j=0,len(pal_str)-1
    while(pal_str[i]==pal_str[j]):
    
       
        if(i<=j and i<len(pal_str) and j>0):
        
        
            i+=1
            j-=1
        else:    
            return True
    else:
        return False
            

    
    

def is_reprated(pal_str):
    visted=[0]*26

    for cr in pal_str :
        
        visted[ord(cr)-ord('a')]+=1
        
    max_ele=max(visted)
    print(max_ele)
    if(max_ele == len(pal_str) or max_ele==len(pal_str)-1):
        return True
        
    else:
        return False
    

def min_cuts(pal_str):
    
    if(is_reprated(pal_str)):
        
        return -1
    
    #cheack if string even or odd 
    if(len(pal_str)%2):
        
        return 2 
        
        
    
    if(len(pal_str)%2==0):
        mid=int(len(pal_str)/2)
        if(not is_pal(pal_str[:mid])):
            return 1
            
        elif(is_pal(pal_str[:mid])):
            
            return min_cuts(pal_str[:mid]) 
            
            
            
            
    
def main():
    pal_str="aaaasaaaa"
    

        

    print(min_cuts(pal_str))

main() 
        
