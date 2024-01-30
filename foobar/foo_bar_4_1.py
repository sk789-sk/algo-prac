# You've blown up the LAMBCHOP doomsday device and relieved the bunnies of their work duries -- and now you need to escape from the space station as quickly and as orderly as possible! The bunnies have all gathered in various locations throughout the station, and need to make their way towards the seemingly endless amount of escape pods positioned in other parts of the station. You need to get the numerous bunnies through the various rooms to the escape pods. Unfortunately, the corridors between the rooms can only fit so many bunnies at a time. What's more, many of the corridors were resized to accommodate the LAMBCHOP, so they vary in how many bunnies can move through them at a time. Given the starting room numbers of the groups of bunnies, the room numbers of the escape pods, and how many bunnies can fit through at a time in each direction of every corridor in between, figure out how many bunnies can safely make it to the escape pods at a time at peak.Write a function solution(entrances, exits, path) that takes an array of integers denoting where the groups of gathered bunnies are, an array of integers denoting where the escape pods are located, and an array of an array of integers of the corridors, returning the total number of bunnies that can get through at each time step as an int. The entrances and exits are disjoint and thus will never overlap. The path element path[A][B] = C describes that the corridor going from A to B can fit C bunnies at each time step.  There are at most 50 rooms connected by the corridors and at most 2000000 bunnies that will fit at a time.For example, if you have:

# entrances = [0, 1]
# exits = [4, 5]
# path = [
# Room 0: [0, 0, 4, 6, 0, 0],
# Room 1: [0, 0, 5, 2, 0, 0],
# Room 2: [0, 0, 0, 0, 4, 4],  
# Room 3: [0, 0, 0, 0, 6, 6],  
# Room 4: [0, 0, 0, 0, 0, 0],  
# Room 5: [0, 0, 0, 0, 0, 0],  
# ]

#Then in each time step, the following might happen:0 sends 4/4 bunnies to 2 and 6/6 bunnies to 31 sends 4/5 bunnies to 2 and 2/2 bunnies to 32 sends 4/4 bunnies to 4 and 4/4 bunnies to 5 3 sends 4/6 bunnies to 4 and 4/6 bunnies to 5


#so Each index in the array is array[A][B] = C means that the capcity from room A to B is C

#The given array means that from along the first row for Room 0 the values are the capcities from Room 0 to the other rooms, 

#[0][0] = 0 from r0 to r0 there is a flow of 0  
#[0][1] = 0 form r0 to r1 there is a flow of 0 
#[0][2] = 4 from r0 to r2 there is a flow of 4

#Each room can fit essencially an infinte number of bunnies 2*10^6 is the given

#this then becomes R2 will have a max of 9 coming in and can send out 8 
#R3 has a maximum of 8 coming in and can have a maximum of 10 coming out 
#This results in r3 sending out 8 at most and r2 also sending out 8 at most resulting in a max flow of 16. 

#Ok this is making sense now with how the array is labeled out.

#Next Ex: ([0], [3], [[0, 7, 0, 0], [0, 0, 6, 0], [0, 0, 0, 8], [9, 0, 0, 0]])

#Bunnies are starting at room 0 and ending at room 3. 

#We need to create the graph at first. 

from collections import deque

def solution (s,t,path):

    #Convert the graph into 1 with only 1 source and sink

    def modify_graph(source,sink,path):
        
        room_count = len(path) + 2
        #add 2 for source and sink super nodes in the case where we only have 1 source and sink this adds an extra dummy room
        graph = []

        for i in range(room_count):
            graph.append([0]*room_count)

        #Make the 0th row the super source and the nth row the super sink
        for room_idx in range(len(path)):
            for connected_room__idx in range(len(path)):
                graph[room_idx+1][connected_room__idx+1] = path[room_idx][connected_room__idx]
        

        #The original matrix is surrouded by 1 row and column of 0s. We need to add in the infinity, or 2,000,000 flow for the appropriate locations on the matrix
                
        #Create links from Super Source to original sources            
        for val in source:
            graph[0][val+1] = 2000000 #[]

        #Create link form super sink to original sinks
        for val in sink:
            graph[val+1][room_count-1] = 2000000
        return graph
    
    def ford_fulkerson(graph, source, sink):

        def bfs(graph, source, sink, parent):
            visited = [False] * len(graph)
            queue = deque()
            queue.append(source)
            visited[source] = True
            while queue:
                u = queue.popleft()
                for v, capacity in enumerate(graph[u]):
                    if not visited[v] and capacity > 0:
                        queue.append(v)
                        visited[v] = True
                        parent[v] = u
                        if v == sink:
                            return True
            return False

        n = len(graph)
        parent = [-1] * n
        max_flow = 0

        while bfs(graph, source, sink, parent):
            path_flow = float("inf")
            s = sink
            while s != source:
                path_flow = min(path_flow, graph[parent[s]][s])
                s = parent[s]

            max_flow += path_flow
            v = sink
            while v != source:
                u = parent[v]
                graph[u][v] -= path_flow
                graph[v][u] += path_flow  # Update reverse edge
                v = parent[v]

        return max_flow

    #The Source is 0 the sink is len(path)+1
    
    #Run max flow algorithm with source = 0, sink = len(path+1), graph = output of modified_graph
    graph = modify_graph(s,t,path)

    max_flow = ford_fulkerson(graph,0,len(path)+1)    
    print(max_flow)    
    
    return graph




s = [0,1]
t = [4,5]
path = [[0, 0, 4, 6, 0, 0], [0, 0, 5, 2, 0, 0], [0, 0, 0, 0, 4, 4], [0, 0, 0, 0, 6, 6], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]

solution(s,t,path)







def ford_fulkerson(graph, source, sink):
    def bfs(graph, source, sink, parent):
        visited = [False] * len(graph)
        queue = deque()
        queue.append(source)
        visited[source] = True
        while queue:
            u = queue.popleft()
            for v, capacity in enumerate(graph[u]):
                if not visited[v] and capacity > 0:
                    queue.append(v)
                    visited[v] = True
                    parent[v] = u
                    if v == sink:
                        return True
        return False

    n = len(graph)
    parent = [-1] * n
    max_flow = 0

    while bfs(graph, source, sink, parent):
        path_flow = float("inf")
        s = sink
        while s != source:
            path_flow = min(path_flow, graph[parent[s]][s])
            s = parent[s]

        max_flow += path_flow
        v = sink
        while v != source:
            u = parent[v]
            graph[u][v] -= path_flow
            graph[v][u] += path_flow  # Update reverse edge
            v = parent[v]

    return max_flow

# Example usage
graph = [
    [0, 16, 13, 0, 0, 0],
    [0, 0, 10, 12, 0, 0],
    [0, 4, 0, 0, 14, 0],
    [0, 0, 9, 0, 0, 20],
    [0, 0, 0, 7, 0, 4],
    [0, 0, 0, 0, 0, 0]
]
source, sink = 0, 5
max_flow = ford_fulkerson(graph, source, sink)


print("Maximum flow from source to sink:", max_flow)


graph2 = [[0, 7, 0, 0], [0, 0, 6, 0], [0, 0, 0, 8], [9, 0, 0, 0]]

max_flow = ford_fulkerson(graph2,0,3)

print("Maximum flow from source to sink: graph2", max_flow)


source = [0, 1]
sink = [4, 5]

graph3 = [[0, 0, 4, 6, 0, 0], [0, 0, 5, 2, 0, 0], [0, 0, 0, 0, 4, 4], [0, 0, 0, 0, 6, 6], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]

modified_g3 = [[0,999,999,0,0,0,0,0],
               [0,0,0,4,6,0,0,0],
               [0,0,0,5,2,0,0,0],
               [0,0,0,0,0,4,4,0],
               [0,0,0,0,0,6,6,0],
               [0,0,0,0,0,0,0,999],
               [0,0,0,0,0,0,0,999],
               [0,0,0,0,0,0,0,0]]

source, sink = 0,7


def modify_graph(s,t,path):
    room_count = len(path) + 2
    #add 2 for source and sink super nodes in the case where we only have 1 source and sink this adds an extra dummy room
    graph = []

    for i in range(room_count):
        graph.append([0]*room_count)

    #Make the 0th row the super source and the nth row the super sink
    for room_idx in range(len(path)):
        for connected_room__idx in range(len(path)):
            graph[room_idx+1][connected_room__idx+1] = path[room_idx][connected_room__idx]
    

    #The original matrix is surrouded by 1 row and column of 0s. We need to add in the infinity, or 2,000,000 flow for the appropriate locations on the matrix
            
    #Create links from Super Source to original sources            
    for val in s:
        graph[0][val+1] = 2000000 #[]

    #Create link form super sink to original sinks
    for val in t:
        graph[val+1][room_count-1] = 2000000
    return s,t,graph

max_flow = ford_fulkerson(modified_g3,source,sink)

print("Maximum flow from source to sink: graph3", max_flow)

print(modify_graph([0,1],[4,5],graph3))