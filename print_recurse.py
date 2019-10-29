#1234567
def print_num(n):
    if(n):
        
        print_num(int(n/10))
        print("step")
        print(n%10)
        
        
print_num(214)    

#214 /10 =21.4 ,21 ,r=4 ->21/10=2.1 ,2 ,r=1 ->2/10= 0 ,r=2 ->stops here and begins printing 

#1234567/10 =123456.7 -> I=123456 ,r=7 
print(2//10)
