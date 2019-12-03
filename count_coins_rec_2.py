
# we have set of coins 100 dollar and  5 ,10 ,20 etc we want to  find all possible combinations of banknotes to form a number n say n=20 c 


#banknotes=[5,10,20,50,100,200,1000]
#eg n=20
#pocket is str to append coins in the sa,e solution 

def comine_coins(curr_rem,coins_stack,pocket,banknotes):

     
       
    if(curr_rem==0):
        print(pocket)
        return pocket
    
    for note in banknotes:
        p=comine_coins(curr_rem-note,coins_stack,pocket+str(note),banknotes)

        
    return p
        

def main():
    n=20
    coins_stack=[]
    banknotes=[5,10,20,50,100,200,1000]
    
    p=(comine_coins(n,coins_stack,"",banknotes))
    
    print(p)
    
main()    
