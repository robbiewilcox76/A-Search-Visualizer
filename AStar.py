from States import States
from MinHeap import MinHeap
from Maze import Maze
from Node import Node
class AStar:
    
    @staticmethod
    def execute(initial, goal, maze, visited):
        current = Node(initial, goal, 0, 0)  #current spot
        heap = MinHeap() # heap for expansion
        heap.addNode(current) #add current move to heap
        counter = 0
        moves = [] #array to backtrack when solution is found
        #heap.toString()
        NodesNextToCur = []
        while(not heap.isEmpty()):
            #if(counter > 75000): 
                #maze.print_maze()
                ##print("terminated")
                #print(goal)
                #print(NodesNextToCur)
                #return
            current = heap.pop() #pick least expensive move
            if current.position == goal:
                #print("hi")
                #print(current.total_cost)
                #print(heap.arr[1].total_cost)
                NodesNextToCur.append(current)
                if(heap.arr[1].total_cost >= current.total_cost):
                    lowest = NodesNextToCur[0]
                    current = lowest
                    for node in NodesNextToCur:
                        if(lowest.total_cost > node.total_cost):
                            current = node
                    AStar.addPath(moves, maze, initial, current.parent)
                    maze.print_maze()
                    #print(NodesNextToCur)
                    return
                else: continue
            moves.append(current) #save move
            visited[current.position[0]][current.position[1]] = 1 #mark as visited
            counter += 1
            AStar.expand(visited, current, maze, heap, counter) #expand from spot
        maze.print_maze()
        print("No solution bozo.") #no solution if heap is empty
            

    #looks complicated but all it does is add nodes that arent blocked to heap with f(n) and changes characters so they print in red
    @staticmethod
    def expand(visited, current, maze, heap, counter): 
        if current.position[0]-1 >= 0:
            if visited[current.position[0]-1][current.position[1]] != 1 and maze.grid[current.position[0]-1][current.position[1]] != 1:
                totalCost = current.step_cost + 1 + maze.manhattans[current.position[0]-1][current.position[1]] 
                heap.addNode(Node([current.position[0]-1, current.position[1]], current, totalCost, current.step_cost+1))
                if maze.grid[current.position[0]-1][current.position[1]] != 3:
                    maze.grid[current.position[0]-1][current.position[1]] = '*'

        if current.position[1]-1 >= 0:
            if visited[current.position[0]][current.position[1]-1] != 1 and maze.grid[current.position[0]][current.position[1]-1] != 1:
                totalCost = current.step_cost + 1 + maze.manhattans[current.position[0]][current.position[1]-1] 
                heap.addNode(Node([current.position[0], current.position[1]-1], current, totalCost, current.step_cost+1))
                if maze.grid[current.position[0]][current.position[1]-1] != 3:
                    maze.grid[current.position[0]][current.position[1]-1] = '*'

        if current.position[0]+1 < 101:
            if visited[current.position[0]+1][current.position[1]] != 1 and maze.grid[current.position[0]+1][current.position[1]] != 1:
                totalCost = current.step_cost + 1 + maze.manhattans[current.position[0]+1][current.position[1]] 
                heap.addNode(Node([current.position[0]+1, current.position[1]], current, totalCost, current.step_cost+1))
                if maze.grid[current.position[0]+1][current.position[1]] != 3:
                    maze.grid[current.position[0]+1][current.position[1]] = '*'

        if current.position[1]+1 < 101:
            if visited[current.position[0]][current.position[1]+1] != 1 and maze.grid[current.position[0]][current.position[1]+1] != 1:
                totalCost = current.step_cost + 1 + maze.manhattans[current.position[0]][current.position[1]+1] 
                heap.addNode(Node([current.position[0], current.position[1]+1], current, totalCost, current.step_cost+1))
                if maze.grid[current.position[0]][current.position[1]+1] != 3:
                    maze.grid[current.position[0]][current.position[1]+1] = '*'
        #heap.toString()

    #should print real shortest path in green, might be kind of off
    @staticmethod
    def addPath(moves, maze, initial, curNode):
        while(curNode.position != initial):
            maze.grid[curNode.position[0]][curNode.position[1]] = '@'
            curNode = curNode.parent

