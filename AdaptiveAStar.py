from AStar import AStar
from Maze import Maze
from Node import Node
import copy

dx = (0,1,0,-1)
dy = (1,0,-1,0)

class AdaptiveAStar:
    expandedNodes = 0
    
    def __init__(self, initial, goal, real_maze, maze_size):
        self.prevManhattans = real_maze.manhattans
        self.current = initial
        self.goal = goal
        self.real_maze = real_maze
        self.maze_size = maze_size
        self.maze = Maze(maze_size)
        self.maze.empty_maze(initial, goal)
            
        #print("Real maze : \n")
        #self.real_maze.print_maze()
        # Explore 4 cells adjacent to neighbor
        self.explore()
        
    def explore(self):
        for i in range(4):
            newX = self.current[0] + dx[i]
            newY = self.current[1] + dy[i]
            if (not self.real_maze.walkable(newX, newY)):
                if (newX >= 0 and newX < self.maze_size and newY >= 0 and newY < self.maze_size):
                   self.maze.grid[newX][newY] = 1
            # else:
            #     if (self.maze.grid[newX][newY] != 2 and self.maze.grid[newX][newY] != 3): 
            #         self.maze.grid[newX][newY] = 6
        
    def execute(self, manhattans, maze):
        if self.current == self.goal: 
            AdaptiveAStar.addPath(maze, [maze.startX, maze.startY], move)
            # maze.print_maze()
            #print("REACHED THE GOAL")
            #print("Total nodes expanded {}".format(AdaptiveAStar.expandedNodes))
            return
        # Get shortest path based on maze that object perceived
        DummyMaze = self.copyMaze()
        DummyMaze.manhattans = manhattans
        
        #if AStar.targNode != None: print("Cost: {}".format(AStar.targNode.step_cost))
        #for node in AStar.expandedArr:
        #    print(node.position)
        for i in range(1, len(AStar.expandedArr)):
            #print("{}".format(AStar.targNode.step_cost - AStar.expandedArr[i].step_cost == DummyMaze.manhattans[AStar.expandedArr[i].position[0]][AStar.expandedArr[i].position[1]]))
            DummyMaze.manhattans[AStar.expandedArr[i].position[0]][AStar.expandedArr[i].position[1]] = AStar.targNode.step_cost - AStar.expandedArr[i].step_cost + 1
        AStar.expandedArr = []
        DummyVisited = self.newVisited()

       # for i in range(len(DummyMaze.manhattans)):
       #     print(DummyMaze.manhattans[i])
       # print("")

        #print(DummyMaze.manhattans == self.real_maze.manhattans)
        # move is pointer to shortest path linkedlist
        move = AStar.execute(self.current, self.goal, DummyMaze, DummyVisited)
        AdaptiveAStar.expandedNodes += AStar.expandedNodes
        # self.visualizeAStar(move)
        if (move): 
            nextX = move.position[0]
            nextY = move.position[1]
            # maze.grid[nextX][nextY]=5
            walkable = self.real_maze.walkable(nextX, nextY)
            while (walkable):
                # Mark current position to be empty
                self.maze.grid[self.current[0]][self.current[1]] = 0
                # Take walk
                self.current[0] = nextX
                self.current[1] = nextY
                # Mark walk step where object has moved
                self.maze.grid[self.current[0]][self.current[1]] = 2
                if maze.grid[nextX][nextY]!=2 and maze.grid[nextX][nextY]!=3:
                    maze.grid[nextX][nextY]=5
                # Take note of the current map
                self.explore()
                # Examine next move / Return if out of moves
                if (not move.parent): 
                    if self.current == self.goal: 
                        # AdaptiveAStar.addPath(maze, [maze.startX, maze.startY], move)
                        # self.maze.print_maze()
                        # maze.print_maze()
                        #print("REACHED THE GOAL")
                        #print("Total nodes expanded {}".format(AdaptiveAStar.expandedNodes))
                        return move
                move = move.parent
                nextX = move.position[0]
                nextY = move.position[1]
                walkable = self.real_maze.walkable(nextX, nextY)
            # Execute until reach the goal OR not walkable (approach obstacles)
            #self.maze.print_maze()
            self.clearMazePath()
            self.execute(DummyMaze.manhattans, maze)
            
        else:
            #print("No Solution")
            return
        
    def visualizeAStar(self, move):
        while (move):
            if (self.maze.grid[move.position[0]][move.position[1]] != 2 and self.maze.grid[move.position[0]][move.position[1]] != 3):
                self.maze.grid[move.position[0]][move.position[1]] = 5
            move = move.parent
            
        #self.maze.print_maze()
    
    def copyMaze(self):
        dummyMaze = copy.deepcopy(self.maze)
        return dummyMaze

    def newVisited(self):
        visited = []
        for i in range(self.maze_size):
            lvl = []
            for j in range(self.maze_size):
                lvl.append(0)
            visited.append(lvl)
        return visited
    
    def clearMazePath(self):
        for i in range(self.maze_size):
            for j in range(self.maze_size):
                if self.maze.grid[i][j] == 5:
                    self.maze.grid[i][j] = 0
        
    #should print real shortest path in green, might be kind of off
    def addPath(maze, initial, curNode):
        # Visualize maze
        if curNode == None: return
        saveNode = curNode
        while(curNode.position != initial):
            AStar.pathNodes+=1
            if (maze.grid[curNode.position[0]][curNode.position[1]] != 2 and maze.grid[curNode.position[0]][curNode.position[1]] != 3):
                maze.grid[curNode.position[0]][curNode.position[1]] = 6
            curNode = curNode.parent
            if curNode == None: return
        
        # reverse linkedlist and return
        ptr_from_start = AStar.reversePath(saveNode)
        return ptr_from_start