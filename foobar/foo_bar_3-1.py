# You're awfully close to destroying the LAMBCHOP doomsday device and freeing Commander Lambda's bunny workers, but once they're free of the work duties the bunnies are going to need to escape Lambda's space station via the escape pods as quickly as possible. Unfortunately, the halls of the space station are a maze of corridors and dead ends that will be a deathtrap for the escaping bunnies. 

#Fortunately, Commander Lambda has put you in charge of a remodeling project that will give you the opportunity to make things a little easier for the bunnies. Unfortunately (again), you can't just remove all obstacles between the bunnies and the escape pods - at most you can remove one wall per escape pod path, both to maintain structural integrity of the station and to avoid arousing Commander Lambda's suspicions.
#You have maps of parts of the space station, each starting at a work area exit and ending at the door to an escape pod.
# The map is represented as a matrix of 0s and 1s, where 0s are passable space and 1s are impassable walls. The door out of the station is at the top left (0,0) and the door into an escape pod is at the bottom right (w-1,h-1). Write a function solution(map) that generates the length of the shortest path from the station door to the escape pod, where you are allowed to remove one wall as part of your remodeling plans.
# The path length is the total number of nodes you pass through, counting both the entrance and exit nodes. The starting and ending positions are always passable (0). The map will always be solvable, though you may or may not need to remove a wall. The height and width of the map can be from 2 to 20. Moves can only be made in cardinal directions; no diagonal moves are allowed.

from collections import deque

def solution(map):
    
    
# #This is a matrix and i need to find the path from the start to the end. 
# #this is just finding the shortest path in a graph no?
# #I can convert the matrix into a graph. The edges are all equal value of 1. 
# #we can give nodes a value of 1 or 0. 1 bieng a wall that needs to be broken
# #Use a traversal algorithm to find the path to the end where we only pass through 1 wall or 0 walls.
# #Whatever is the shortest path form those is the path to the end and its length is my answer.
#Do i even need to do a full traversal?
    
#I think the issue is that since we do not have a do not visit list again, we are checking alot of dead paths. In normal BFS we do not repeat visit a node. That isnt true for this cause since if we visit a node with a 0 walls in the path we do not need to revisit it If we visit a node that has a 0 in the path than we do not need to revisit it. Basically we can revisit a node upto 1 time in this BFS which i need to add. 
    
        
    graph = {}

    visit_dict = {}
    
    for row_idx, row in enumerate(map):
        row_max = len(map)
        for column_idx,val in enumerate(row):
            col_max = len(row)            
            graph[f'{row_idx},{column_idx}'] = {'value':val , 'neighbor': []}
            
            visit_dict[f'{row_idx},{column_idx}'] = 10

            #need to check that we are within bounds as well

            #down and to the right first 

            if column_idx+1 in range(0,col_max):
                down = f'{row_idx},{column_idx+1}'
                graph[f'{row_idx},{column_idx}']['neighbor'].append(down)
            if row_idx+1 in range(0,row_max):
                right = f'{row_idx+1},{column_idx}'
                graph[f'{row_idx},{column_idx}']['neighbor'].append(right)
            if column_idx-1 in range(0,col_max):               
                up = f'{row_idx},{column_idx-1}'
                graph[f'{row_idx},{column_idx}']['neighbor'].append(up)
            if row_idx-1 in range(0,row_max):
                left = f'{row_idx-1},{column_idx}'
                graph[f'{row_idx},{column_idx}']['neighbor'].append(left)



    #Now we need to find the path to vertex[row_max,col_max] starting from [0,0]

    goal = f'{row_max-1},{col_max-1}'


    #vertexes are (id, cost to arrive, path list of strings)
    start = (f'0,0',0,[]) #the -1,-1 is the step into the start or i can do +2 at the end

    visit_que = deque()
    visit_que.append(start)

    while visit_que:
        
        vertex = visit_que.popleft() #(id,cost,path)

        #We have arrived at vertex with a cost of x. 

        if vertex[0] == goal:
            print(vertex[2] + [vertex[0]])
            print(visit_dict)
            return len(vertex[2])+1

        cost_to_pass = graph[vertex[0]]['value']

        #Scenarios:
        #1. we have arrived at the vertex at cost 0 and we have a path with cost 0 already #do not add vertex neighbors to visit que
        #2. We have arrived at the vertex at cost 0 and we have a path with cost 1 already #Search we may need this
        #3. We have arrived at the vertex at a cost 1 and we have a path with cost 0 already #Do not add vertex neighbors
        #4. We have arrived at the vertex at cost 1 and we have a path with cost 1 already #Do not add vertex neighbors
        #5. We have arrived at the vertex with a cost of 1 and cost through the vertex is 1 #Do not add vertex neighbors
        #6 We have arrived at the vertex with a cost of 1, and have not visited the vertex yet. #Search look at neighbors

        if vertex[1] == cost_to_pass == 1: #5
            continue
        
        #this can just be 1 if else

        if vertex[1] >= visit_dict[vertex[0]]: #1,3,4
            continue

        if vertex[1] < visit_dict[vertex[0]]: #2,6
            #look at the neighbors. 
            #We have a path to this vertex with a cost of cost to arrive and cost to pass that needs to go to the dict
            visit_dict[vertex[0]] = vertex[1] + cost_to_pass
    
            for val in graph[vertex[0]]['neighbor'] : #lets go over the neighbors list
                    #if the neighbor is not in the path to arrive. Prevent the addition of A->B->A
                    if val not in vertex[2]:
                        path = vertex[2] + [vertex[0]]
                        cost = vertex[1] + cost_to_pass #Cost to arrive at previos vertex and pass through it
                        new_vertex = (val,cost,path)
                        visit_que.append(new_vertex)

                #create the new vertex to explore and add it to the visit_que
    return -1 #unsolvable            
        
# matrix = [[0, 0, 0, 0, 0, 0,0], [1, 1, 1, 1, 1, 0,0], [0, 0, 0, 0, 0, 0,0], [0, 1, 1, 1, 1, 1,0], [0,0, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0,0],[0,0,0,0,0,0,0]]

# matrix = [[0,1,0,1],[0,0,1,1],[0,1,0,0]]

# matrix = [[0,0,0],[0,0,0],[0,0,0],[0,0,0]]

# matrix = [[1,1,1],[1,1,1],[1,1,1]]

# matrix = [[0, 1, 1, 0], [0, 0, 0, 1], [1, 1, 0, 0], [1, 1, 1, 0]]

# matrix = [[0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0]]

matrix = [[0, 0, 0, 0, 0, 0],[1, 1, 1, 1, 1, 0],[1, 1, 1, 1, 1, 1],[0, 0, 0, 0, 0, 0],[0, 1, 1, 1, 1, 1],[0, 0, 0, 0, 0, 0]] #Answer 21

matrix = [[0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0]]



print(solution(matrix))






#2.7 

def solution2_7(map):
    
    
    graph = {}
    visit_dict = {}
    
    
    for row_idx, row in enumerate(map):
        row_max = len(map)
        for column_idx,val in enumerate(row):
            col_max = len(row)
            # print(row_idx,column_idx)
            # print(f'value in cell is {val}')
            
            graph['{},{}'.format(row_idx,column_idx)] = {'value':val , 'neighbor': []}
            
            visit_dict['{},{}'.format(row_idx,column_idx)] = 10

            
            #need to check that we are within bounds as well
            if column_idx+1 in range(0,col_max):
                down = '{},{}'.format(row_idx,column_idx+1)
                graph['{},{}'.format(row_idx,column_idx)]['neighbor'].append(down)
            if row_idx+1 in range(0,row_max):
                right = '{},{}'.format(row_idx+1,column_idx)
                graph['{},{}'.format(row_idx,column_idx)]['neighbor'].append(right)
            if column_idx-1 in range(0,col_max):               
                up = '{},{}'.format(row_idx,column_idx-1)
                graph['{},{}'.format(row_idx,column_idx)]['neighbor'].append(up)
            if row_idx-1 in range(0,row_max):
                left = '{},{}'.format(row_idx-1,column_idx)
                graph['{},{}'.format(row_idx,column_idx)]['neighbor'].append(left)

    #Now we need to find the path to vertex[row_max,col_max] starting from [0,0]

    goal = '{},{}'.format(row_max-1,col_max-1)

    start = ('0,0',0,[]) 
    
    visit_que = deque()
    visit_que.append(start)
    
    while visit_que:
        vertex = visit_que.popleft() #(id,cost,path)
        
        if vertex[0] == goal:
            return len(vertex[2])+1

        cost_to_pass = graph[vertex[0]]['value']

        #Scenarios:
        #1. we have arrived at the vertex at cost 0 and we have a path with cost 0 already #do not add vertex neighbors to visit que
        #2. We have arrived at the vertex at cost 0 and we have a path with cost 1 already #Search we may need this
        #3. We have arrived at the vertex at a cost 1 and we have a path with cost 0 already #Do not add vertex neighbors
        #4. We have arrived at the vertex at cost 1 and we have a path with cost 1 already #Do not add vertex neighbors
        #5. We have arrived at the vertex with a cost of 1 and cost through the vertex is 1 #Do not add vertex neighbors
        #6 We have arrived at the vertex with a cost of 1, and have not visited the vertex yet. #Search look at neighbors

        if vertex[1] == cost_to_pass == 1: #5
            continue
        
        #this can just be 1 if else

        if vertex[1] >= visit_dict[vertex[0]]: #1,3,4
            continue

        if vertex[1] < visit_dict[vertex[0]]: #2,6
            #look at the neighbors. 
            #We have a path to this vertex with a cost of cost to arrive and cost to pass that needs to go to the dict
            visit_dict[vertex[0]] = vertex[1] + cost_to_pass
    
            for val in graph[vertex[0]]['neighbor'] : #lets go over the neighbors list
                    #if the neighbor is not in the path to arrive. Prevent the addition of A->B->A
                    if val not in vertex[2]:
                        path = vertex[2] + [vertex[0]]
                        cost = vertex[1] + cost_to_pass #Cost to arrive at previos vertex and pass through it
                        new_vertex = (val,cost,path)
                        visit_que.append(new_vertex)
        
    
    return -1 #unsolvable

