from States import States
from MinHeap import MinHeap
from Maze import Maze
from Node import Node
from gridworld import reload
import copy
class AStar:
    expandedNodes = -1
    pathNodes = 0
    
    @staticmethod
    def execute(initial, goal, maze, visited):
        current = Node(initial, None, 0, 0)  #current spot
        heap = MinHeap() # heap for expansion
        heap.addNode(current) #add current move to heap
        counter = 0
        moves = [] #array to backtrack when solution is found
        while(not heap.isEmpty()):
            current = heap.pop() #pick least expensive move
            visited[current.position[0]][current.position[1]] = 1 #mark as visited
            if current.position == goal:
                moves = AStar.addPath(maze, initial, current)
                print("Number of nodes expanded: {}".format(AStar.expandedNodes))
                print("Number of nodes in shortest path: {}".format(AStar.pathNodes))
                # for move in moves:
                #     print('(', move.position[0], ',', move.position[1], ')')
                # print("Maze from AStar: \n")
                # maze.print_maze()
                return moves
            counter += 1
            AStar.expand(visited, current, maze, heap, counter) #expand from spot
            AStar.expandedNodes+=1
        
        maze.print_maze()
        print("No solution bozo.") #no solution if heap is empty
        print("Number of nodes expanded: {}".format(AStar.expandedNodes))
        print("Number of nodes in shortest path: {}".format(AStar.pathNodes))
        return []
            
    #looks complicated but all it does is add nodes that arent blocked to heap with f(n) and changes characters so they print in red
    @staticmethod
    def expand(visited, current, maze, heap, counter): 
        if current.position[0]-1 >= 0:
            if visited[current.position[0]-1][current.position[1]] != 1 and maze.grid[current.position[0]-1][current.position[1]] != 1:
                totalCost = current.step_cost + 1 + maze.manhattans[current.position[0]-1][current.position[1]] 
                heap.addNode(Node([current.position[0]-1, current.position[1]], current, totalCost, current.step_cost+1))
                if maze.grid[current.position[0]-1][current.position[1]] != 3:
                    maze.grid[current.position[0]-1][current.position[1]] = 6#'*'

        if current.position[1]-1 >= 0:
            if visited[current.position[0]][current.position[1]-1] != 1 and maze.grid[current.position[0]][current.position[1]-1] != 1:
                totalCost = current.step_cost + 1 + maze.manhattans[current.position[0]][current.position[1]-1] 
                heap.addNode(Node([current.position[0], current.position[1]-1], current, totalCost, current.step_cost+1))
                if maze.grid[current.position[0]][current.position[1]-1] != 3:
                    maze.grid[current.position[0]][current.position[1]-1] = 6#'*'

        if current.position[0]+1 < len(maze.grid):
            if visited[current.position[0]+1][current.position[1]] != 1 and maze.grid[current.position[0]+1][current.position[1]] != 1:
                totalCost = current.step_cost + 1 + maze.manhattans[current.position[0]+1][current.position[1]] 
                heap.addNode(Node([current.position[0]+1, current.position[1]], current, totalCost, current.step_cost+1))
                if maze.grid[current.position[0]+1][current.position[1]] != 3:
                    maze.grid[current.position[0]+1][current.position[1]] = 6#'*'

        if current.position[1]+1 < len(maze.grid):
            if visited[current.position[0]][current.position[1]+1] != 1 and maze.grid[current.position[0]][current.position[1]+1] != 1:
                totalCost = current.step_cost + 1 + maze.manhattans[current.position[0]][current.position[1]+1] 
                heap.addNode(Node([current.position[0], current.position[1]+1], current, totalCost, current.step_cost+1))

                if maze.grid[current.position[0]][current.position[1]+1] != 3:
                    maze.grid[current.position[0]][current.position[1]+1] = 6#'*'


    #should print real shortest path in green, might be kind of off
    @staticmethod
    def addPath(maze, initial, curNode):
        moves = []
        while(curNode.position != initial):
            AStar.pathNodes+=1
            moves.append(curNode)
            if (maze.grid[curNode.position[0]][curNode.position[1]] != 2 and maze.grid[curNode.position[0]][curNode.position[1]] != 3):
                maze.grid[curNode.position[0]][curNode.position[1]] = 5
            curNode = curNode.parent
        return moves

    @staticmethod
    def RepeatedAStar(initial, goal, maze, visited, realMaze): ##arr is the current maze from the agents point of view
        newMaze = copy.deepcopy(maze)
        newMaze.empty_maze()
        maze.check_walls(newMaze.grid, initial[0], initial[1]) #adds walls next to agent start
        visited = [[0 for i in range(101)] for j in range(101)] #creates visited array
        AStar.execute(initial, goal, newMaze, visited, realMaze)
        maze.print_maze()