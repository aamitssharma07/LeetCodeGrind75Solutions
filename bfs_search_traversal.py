

#This function will give the adjacent vertices
def adjacent_vertex(vertex):
    adj_vertex = []
    for x in range(len(G)):
        if(G[vertex][x]==1):
            adj_vertex.append(x)
    return adj_vertex

#This function will will do the bfs
def BFS(vertex):
    bfs_search = []    
    while(len(explore_queue)!=0):
        explore_vertex = explore_queue.pop(0)
        bfs_search.append(explore_vertex)
        adjacent_vertices = adjacent_vertex(explore_vertex)       
        for x in adjacent_vertices:
            if(visited_queue[x]==0):
                visited_queue[x]=1
                explore_queue.append(x) 
    return bfs_search  

#If graph is disconnected and you want to reach every node then you have to use graph traverse
def BFS_Traverse(vertex):    
    BFS_traverse_vertex  =  BFS(vertex)
    for index, value  in enumerate(visited_queue):
        if(value==0):     
            explore_queue.append(index)   
            visited_queue[index]=1   
            BFS_traverse_vertex = BFS_traverse_vertex + BFS(index)
    return BFS_traverse_vertex 
        
    
    
    
    
# G1 = [[0,1,1,1],[1,0,0,1],[1,0,0,1],[1,1,1,0]]   #Connected Graph

G= [[0,1,1,1,0,0],[1,0,0,1,0,0],[1,0,0,1,0,0],[1,1,1,0,0,0],[0,0,0,0,0,1],[0,0,0,0,1,0]] # Disconnected graph, for reaching each vertex of this graph we chave to call traversal

vertex = 0
#Initializing vistited queqe with 0
visited_queue = []
for x in range(len(G)):
    visited_queue.append(0)
visited_queue[vertex]=1

explore_queue = []
explore_queue.append(vertex)       
# bfs_search = BFS(vertex)

bfs_traverse =BFS_Traverse(G)
print(bfs_traverse)

    