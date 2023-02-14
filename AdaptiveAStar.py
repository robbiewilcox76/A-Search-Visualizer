from States import States
from MinHeap import MinHeap
from Maze import Maze
from Node import Node
from gridworld import reload
from AStar import AStar
import copy
class adaptiveAStar:
    expandedNodes = -1
    pathNodes = 0
    @staticmethod
    def heuristicount(maze):
        blankmaze=[]
        for i in range(0,maze.height):
            lvl=[]
            for j in range(0,maze.width):
                if maze.grid[i][j]==2:
                    lvl.append(2)
                if maze.grid[i][j]==3:
                    lvl.append(3)
                else:
                    lvl.append(0)
            blankmaze.append(lvl)
        # blankmaze[100][100]=1
        return blankmaze
        
    @staticmethod
    def adaptive(initial, goal, maze, visited):
        current = Node(initial, None, 0, 0)  #current spot
        heap = MinHeap() # heap for expansion
        heap.addNode(current) #add current move to heap
        counter = 0
        moves = []
        from AdaptiveAStar import adaptiveAStar
        knownmaze=adaptiveAStar.heuristicount(maze)

        maze2=Maze(101)
        maze2.grid=knownmaze
        for i in range(0,maze.height):
            lvl=[]
            for j in range(0,maze.width):
                lvl.append(maze.manhattans[i][j])
            maze2.manhattans.append(lvl)

        # for i in range(101):
        #     for j in range (101):
        #         print(maze.grid[i][j])
        # AStar.execute(initial, goal, maze2, visited2)
        # dist=0
        # x=goal[0]
        # y=goal[1]
        # goal
        while(not heap.isEmpty()):
            current = heap.pop() #pick least expensive move
            visited[current.position[0]][current.position[1]] = 1 #mark as visited
            # adaptiveAStar.update(current.position, goal, maze2, maze)
            if current.position == goal:
                moves = AStar.addPath(maze, initial, current)
                print("Number of nodes expanded: {}".format(adaptiveAStar.expandedNodes))
                print("Number of nodes in shortest path: {}".format(adaptiveAStar.pathNodes))
                # for move in moves:
                #     print('(', move.position[0], ',', move.position[1], ')')
                # print("Maze from AStar: \n")
                # maze.print_maze()
                return moves
            counter += 1
            adaptiveAStar.expand(visited, current, maze, heap, counter, maze2) #expand from spot
            adaptiveAStar.expandedNodes+=1
        
        maze.print_maze()
        print("No solution bozo.") #no solution if heap is empty
        print("Number of nodes expanded: {}".format(adaptiveAStar.expandedNodes))
        print("Number of nodes in shortest path: {}".format(adaptiveAStar.pathNodes))
        return []
            
    #looks complicated but all it does is add nodes that arent blocked to heap with f(n) and changes characters so they print in red and updates heuristic
    @staticmethod
    def expand(visited, current, maze, heap, counter, maze2): 
        if current.position[0]-1 >= 0:
            if maze.grid[current.position[0]-1][current.position[1]]==6:
                maze2.grid[current.position[0]-1][current.position[1]]=0
            else:
                maze2.grid[current.position[0]-1][current.position[1]]=maze.grid[current.position[0]-1][current.position[1]]
            if visited[current.position[0]-1][current.position[1]] != 1 and maze.grid[current.position[0]-1][current.position[1]] != 1:
                # goal=[maze.targetX, maze.targetY]
                # adaptiveAStar.update(current.position, goal, maze2, maze)
                x=current.position[0]
                y=current.position[1]
                totalCost = current.step_cost + 1 + maze.manhattans[x-1][y] 
                heap.addNode(Node([current.position[0]-1, current.position[1]], current, totalCost, current.step_cost+1))
                if maze.grid[current.position[0]-1][current.position[1]] != 3 and maze.grid[current.position[0]-1][current.position[1]] != 2:
                    maze.grid[current.position[0]-1][current.position[1]] = 6#'*'

        if current.position[1]-1 >= 0:
            if maze.grid[current.position[0]][current.position[1]-1]==6:
                maze2.grid[current.position[0]][current.position[1]-1]=0
            else:
                maze2.grid[current.position[0]][current.position[1]-1]=maze.grid[current.position[0]][current.position[1]-1]
            if visited[current.position[0]][current.position[1]-1] != 1 and maze.grid[current.position[0]][current.position[1]-1] != 1:
                # goal=[maze.targetX, maze.targetY]
                # adaptiveAStar.update(current.position, goal, maze2, maze)
                x=current.position[0]
                y=current.position[1]               
                totalCost = current.step_cost + 1 + maze.manhattans[x][y-1] 
                heap.addNode(Node([current.position[0], current.position[1]-1], current, totalCost, current.step_cost+1))
                if maze.grid[current.position[0]][current.position[1]-1] != 3 and maze.grid[current.position[0]][current.position[1]-1] != 2:
                    maze.grid[current.position[0]][current.position[1]-1] = 6#'*'

        if current.position[0]+1 < len(maze.grid):
            if maze.grid[current.position[0]+1][current.position[1]]==6:
                maze2.grid[current.position[0]+1][current.position[1]]=0
            else:
                maze2.grid[current.position[0]+1][current.position[1]]=maze.grid[current.position[0]+1][current.position[1]]
            if visited[current.position[0]+1][current.position[1]] != 1 and maze.grid[current.position[0]+1][current.position[1]] != 1:
                # goal=[maze.targetX, maze.targetY]
                # adaptiveAStar.update(current.position, goal, maze2, maze)
                x=current.position[0]
                y=current.position[1]
                totalCost = current.step_cost + 1 + maze.manhattans[x+1][y] 
                heap.addNode(Node([current.position[0]+1, current.position[1]], current, totalCost, current.step_cost+1))
                if maze.grid[current.position[0]+1][current.position[1]] != 3 and maze.grid[current.position[0]+1][current.position[1]] != 2:
                    maze.grid[current.position[0]+1][current.position[1]] = 6#'*'

        if current.position[1]+1 < len(maze.grid):
            if maze.grid[current.position[0]][current.position[1]+1]==6:
                maze2.grid[current.position[0]][current.position[1]+1]=0
            else:
                maze2.grid[current.position[0]][current.position[1]+1]=maze.grid[current.position[0]][current.position[1]+1]
            if visited[current.position[0]][current.position[1]+1] != 1 and maze.grid[current.position[0]][current.position[1]+1] != 1:
                # goal=[maze.targetX, maze.targetY]
                # adaptiveAStar.update(current.position, goal, maze2, maze)   
                x=current.position[0]
                y=current.position[1]             
                totalCost = current.step_cost + 1 + maze.manhattans[x][y+1] 
                heap.addNode(Node([current.position[0], current.position[1]+1], current, totalCost, current.step_cost+1))
                if maze.grid[current.position[0]][current.position[1]+1] != 3 and maze.grid[current.position[0]][current.position[1]+1] != 2:
                    maze.grid[current.position[0]][current.position[1]+1] = 6#'*'
        goal=[maze.targetX, maze.targetY]
        adaptiveAStar.update(current.position, goal, maze2, maze)         
    @staticmethod
    def update(initial, goal, maze2, maze):
        # print(initial[0])
        # print(initial[1])
        visited2=[]
        for i in range(101):
            lvl = []
            for j in range(101):
                lvl.append(0)
            visited2.append(lvl)
        AStar.execute(initial, goal, maze2, visited2)
        dist=0
        x=goal[0]
        y=goal[1]
        while x!=initial[0] and y!=initial[1]:
            dist+=1
            maze.manhattans[x][y]=dist
            maze2.manhattans=dist
            # print(maze2.grid[x][y])
            if x>0:
                if maze2.grid[x-1][y]==5 or maze2.grid[x-1][y]==2:
                    maze2.grid[x][y]=0
                    x=x-1
                    # print("a")
                    continue
            if y>0:
                if maze2.grid[x][y-1]==5 or maze2.grid[x][y-1]==2:
                    maze2.grid[x][y]=0
                    y=y-1
                    # print("b")
                    continue
            if x+1<len(maze.grid):
                if maze2.grid[x+1][y]==5 or maze2.grid[x+1][y]==2:
                    maze2.grid[x][y]=0
                    x=x+1
                    # print("c")
                    continue
            if y<=len(maze.grid):
                if maze2.grid[x][y+1]==5 or maze2.grid[x][y+1]==2:
                    maze2.grid[x][y]=0
                    y=y+1
                    # print("d")
                    continue
        AStar.pathReset(maze2)