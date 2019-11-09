#forming teams we got to form 2 teams from list of students there are m pairs of mutually archenimy students and n students 

#archenimy students cant be put together in the same group and the produced groups should be finally equal in size 

# it can be seen as a graph of relations  ----- a node that forms a cycle (share archenimy relations  ) should be removed 

# cycle is a list that will hold all nodes traversed till now untill the function breaks when finding a cycle 
#the dfs fundtion to detect  cycles in the archenimy graph
# we shall output the ppl that we will remove so we can form 2 equal sized coherent teams 
def cycle_dfs(src,adj,cycle,visted):
    if(visted[src]):
        return 
    
    visted[src]=True
    
    cycle.append(src)
    for child in adj[src]:
        if(not visted[child]):
            cycle_dfs(child,adj,cycle,visted)
    return


def form_teams(num_stud,m_arc,adj):
    count=0
    visted=(num_stud+1)*[False]
    
    cycle=[]
    #detect if it was an even cycle or an odd cycle 
    # len(cycle)&1 means that the number of nodes in cycle are odd 
    #cycle[-1] last node before the function breaks 
    # means that this node(forming cycle) has two children
    for src in range(num_stud+1):
        if (not visted[src]):
            cycle_dfs(src,adj,cycle,visted)
            print(cycle)
            if(len(cycle)&1 and len(adj[cycle[-1]])==2):
                count+=1
    # num_stud-count &1 means to check if the total number of students minus the ppl we chose to remove will form an odd count 
    #so satsfying the rule of equal teams we shall remove more +1
    
    if(num_stud-count &1):
        count+=1
        
    return count 
    
def add_edge(u,v,adj):
    
    adj[u].append(v)
    adj[v].append(u)

def main():
    num_stud= 5
    m_arc=4
    adj=[[] for i in range(num_stud+1)]
    
    add_edge(1,2,adj)
    add_edge(2,4,adj)
    add_edge(5,3,adj)
    add_edge(1,4,adj)
    print(adj)
    cont=form_teams(num_stud,m_arc,adj)
    print(cont)
    
main()
    
    
    
            
    
    
    
    
    

