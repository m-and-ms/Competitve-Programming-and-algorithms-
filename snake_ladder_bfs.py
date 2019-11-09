
#bfs shortest path from source to target 
# snake and ladder problem a grid from 1->30 30 src-> target 
#move aaray either =-1 when its a normal cell and = desitanation state when there is a snake or a ladder in the current cell
#move[current]=-1 or move[current]= desitanation
# we want to minmize the no of dice throws to reach the target cell (get the shortest path to tgt using ladders) 
#at each state(node or cell here) the are six reachable states either current+1 or +2 or +3 or +4 or +5 or +6 or a direct acsess to a far away cell through a ladder or a snake   
def get_adj(curnt_node,move_arr,step):

    if(move_arr[curnt_node+step]==-1):
        tgt=curnt_node+step

            
    else:
        
            
        tgt=move_arr[curnt_node+step]

    return tgt   
    
    
    


def bfs(src,tgt,move_arr,visted):
    num_nodes=len(move_arr)
    
    visted=[False]*num_nodes
    
    dist=[-1]*num_nodes
    queue=[]
    
    visted[src]=True
    queue.append(src)
    dist[src]=0
    
    while(len(queue)):
        parent=queue[0]
        queue.pop(0)
        if(parent==tgt):
            break
        for step in range(1,6):
            if(step+parent<num_nodes):
                
                child=get_adj(parent,move_arr,step)
                if(not visted[child]):

                    visted[child]=True
                    queue.append(child)
                
                    dist[child]=dist[parent]+1


    print("dist",dist)           
    return dist[tgt]          
    

    
def main():
    num_nodes=30
    moves=[-1]*num_nodes
    visted=[False]*num_nodes
    # Ladders 
    moves[2] = 21
    moves[4] = 7
    moves[10] = 25
    moves[19] = 28
  
    # Snakes 
    moves[26] = 0
    moves[20] = 8
    moves[16] = 3
    moves[18] = 6
    
    print(bfs(0,num_nodes-1,moves,visted))
    
main()
    
    
