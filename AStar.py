from States import States
from MinHeap import MinHeap
from Maze import Maze
from Node import Node
from gridworld import reload
class AStar:
    expandedNodes = -1
    pathNodes = 0
    
    @staticmethod
    def execute(initial, goal, maze, visited):
        current = Node(initial, goal, 0, 0)  #current spot
        heap = MinHeap() # heap for expansion
        heap.addNode(current) #add current move to heap
        counter = 0
        moves = [] #array to backtrack when solution is found
        NodeNextToCur = None
        while(not heap.isEmpty()):
            current = heap.pop() #pick least expensive move
            if current.position == goal:
                NodeNextToCur = current #Saves node that leads to target
                if heap.arr[1].total_cost >= NodeNextToCur.total_cost: #Compares all paths to target to find lowest one
                    AStar.addPath(moves, maze, initial, current.parent)
                    maze.print_maze()
                    print("Number of nodes expanded: {}".format(AStar.expandedNodes))
                    print("Number of nodes in shortest path: {}".format(AStar.pathNodes))
                    return
                else: continue
            moves.append(current) #save move
            visited[current.position[0]][current.position[1]] = 1 #mark as visited
            counter += 1
            #reload(maze.grid)
            AStar.expand(visited, current, maze, heap, counter) #expand from spot
            AStar.expandedNodes+=1
        maze.print_maze()
        
        print("No solution bozo.") #no solution if heap is empty
        print("Number of nodes expanded: {}".format(AStar.expandedNodes))
        print("Number of nodes in shortest path: {}".format(AStar.pathNodes))
            

    #looks complicated but all it does is add nodes that arent blocked to heap with f(n) and changes characters so they print in red
    @staticmethod
    def expand(visited, current, maze, heap, counter): 
        if current.position[0]-1 >= 0:
            if visited[current.position[0]-1][current.position[1]] != 1 and maze.grid[current.position[0]-1][current.position[1]] != 1:
                totalCost = current.step_cost + 1 + maze.manhattans[current.position[0]-1][current.position[1]] 
                heap.addNode(Node([current.position[0]-1, current.position[1]], current, totalCost, current.step_cost+1))
                #AStar.expandedNodes+=1
                if maze.grid[current.position[0]-1][current.position[1]] != 3:
                    maze.grid[current.position[0]-1][current.position[1]] = 6#'*'

        if current.position[1]-1 >= 0:
            if visited[current.position[0]][current.position[1]-1] != 1 and maze.grid[current.position[0]][current.position[1]-1] != 1:
                totalCost = current.step_cost + 1 + maze.manhattans[current.position[0]][current.position[1]-1] 
                heap.addNode(Node([current.position[0], current.position[1]-1], current, totalCost, current.step_cost+1))
                #AStar.expandedNodes+=1
                if maze.grid[current.position[0]][current.position[1]-1] != 3:
                    maze.grid[current.position[0]][current.position[1]-1] = 6#'*'

        if current.position[0]+1 < len(maze.grid):
            if visited[current.position[0]+1][current.position[1]] != 1 and maze.grid[current.position[0]+1][current.position[1]] != 1:
                totalCost = current.step_cost + 1 + maze.manhattans[current.position[0]+1][current.position[1]] 
                heap.addNode(Node([current.position[0]+1, current.position[1]], current, totalCost, current.step_cost+1))
                #AStar.expandedNodes+=1
                if maze.grid[current.position[0]+1][current.position[1]] != 3:
                    maze.grid[current.position[0]+1][current.position[1]] = 6#'*'

        if current.position[1]+1 < len(maze.grid):
            if visited[current.position[0]][current.position[1]+1] != 1 and maze.grid[current.position[0]][current.position[1]+1] != 1:
                totalCost = current.step_cost + 1 + maze.manhattans[current.position[0]][current.position[1]+1] 
                heap.addNode(Node([current.position[0], current.position[1]+1], current, totalCost, current.step_cost+1))
                #AStar.expandedNodes+=1
                if maze.grid[current.position[0]][current.position[1]+1] != 3:
                    maze.grid[current.position[0]][current.position[1]+1] = 6#'*'

    #should print real shortest path in green, might be kind of off
    @staticmethod
    def addPath(moves, maze, initial, curNode):
        while(curNode.position != initial):
            maze.grid[curNode.position[0]][curNode.position[1]] = 5#'@'
            AStar.pathNodes+=1
            curNode = curNode.parent