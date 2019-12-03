#                                                       R  G  B 
#coloring rgb street input houses ex: n=4    houses = [[1,10,100],[10 ,20,5],[40 ,35,25],[18,70,10]]


def is_valid(last_color,curr_color):
    if(curr_color==last_color):
        return False 
        
    return True                               
    
    


def rgb_street(houses,house,total_cost,last_color,min_cost):
    
    
    
    if(house==len(houses)):
        return total_cost 
    
    if(is_valid(last_color,0)):
        
        costred=rgb_street(houses,house+1,total_cost+houses[house][0],0,min_cost)
        # we painted the current house and go recurse on the next 
        min_cost=min(costred,min_cost)
        
    if(is_valid(last_color,1)):
        
        costgr=rgb_street(houses,house+1,total_cost+houses[house][1],1,min_cost)
        
        min_cost=min(costgr,min_cost)
        
    if(is_valid(last_color,2)):
        costbl=rgb_street(houses,house+1,total_cost+houses[house][2],2,min_cost)
        min_cost=min(costbl,min_cost)
        
        
    return min_cost    
        
        
def main():
    houses = [[1,10,100],[10 ,20,5],[40 ,35,25],[18,70,10]]
    cost=rgb_street(houses,0,0,3,100000000000000000)
    print(cost)
main()    
    
    
    
