from AStar import AStar
from Maze import Maze
from Node import Node

dx = (0,1,0,-1)
dy = (1,0,-1,0)

class RepeatedAStar:
    def __init__(self, initial, goal, real_maze, maze_size):
        self.current = initial
        self.goal = goal
        self.real_maze = real_maze
        self.maze_size = maze_size
        self.maze = Maze(maze_size)
        self.maze.empty_maze(initial, goal)
        visited = []
        for i in range(maze_size):
            lvl = []
            for j in range(maze_size):
                lvl.append(0)
            visited.append(lvl)
            
        self.visited = visited
        print("Perceived Maze: \n")
        self.maze.print_maze()
        print("Real maze : \n")
        self.real_maze.print_maze()
        # Explore 4 cells adjacent to neighbor
        self.explore()
        
    #reverses and returns new head of LL
    def ReversePath(node: Node):
        ptr = node
        prev = None
        while ptr != None:
            next = ptr.parent
            ptr.parent = prev
            prev = ptr
            ptr = next
        return prev
        
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
        
    def execute(self):
        if self.current == self.goal: return
        # Get shortest path based on maze that object perceived
        moves = []
        moves = AStar.execute(self.current, self.goal, self.maze, self.visited)
        # print("Moves in RepeatedAStar is :\n", moves)
        self.visualizeAStar(moves)
        if (moves): 
            # list of moves not empty
            moves.reverse()
            move = moves.pop()
            nextX = move.position[0]
            nextY = move.position[1]
            walkable = self.real_maze.walkable(nextX, nextY)
            counter = 1
            while (walkable):
                # Take walk
                self.current[0] = nextX
                self.current[1] = nextY
                # Mark walk step where object has moved
                self.maze.grid[self.current[0]][self.current[1]] = 2
                # Take note of the current map
                self.explore()
                # Examine next move / Return if out of moves
                if (not moves): return
                move = moves.pop()
                nextX = move.position[0]
                nextY = move.position[1]
                walkable = self.real_maze.walkable(nextX, nextY) 
                print(counter, " walkable is: ", walkable)
            # Execute until reach the goal
            self.execute()
            
        else:
            print("No Solution")
            return
        
    def visualizeAStar(self, moves):
        x = self.maze
        for move in moves:
            if (x.grid[move.position[0]][move.position[1]] != 2 and x.grid[move.position[0]][move.position[1]] != 3):
                x.grid[move.position[0]][move.position[1]] = 5
            
        x.print_maze()
        
        