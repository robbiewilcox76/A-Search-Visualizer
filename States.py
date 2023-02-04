from Maze import Maze
from enum import Enum

class Direction(Enum):
    UP = (0, 1)
    DOWN = (0, -1)
    LEFT = (-1, 0)
    RIGHT = (1, 0)

import math
class States():
    def __init__(self, maze: Maze, initial, goal: int):
        self.current = maze
        self.initial = initial
        self.goal = goal
        
        ## initialize map to check what position we visited
        self.visited = []
        for i in range(101):
            row = [False]*101
            self.visited.append(row)
        for i in range(len(maze.grid)):
            for j in range(len(maze.grid[i])):
                if maze.grid[i][j] == 1:
                    self.visited[i][j] == True
                
    def expand(current):
        moves = []
        for data in Direction:
            newPosition = (current[0] + data.value[0], current[1] + data.value[1])
            if (is_valid(newPosition)):
                moves.append(newPosition)
        return moves
    
    def is_valid(self, current):
        if (current[0] < 0 | current[0] > 101):
            return False
        if (current[1] < 0 | current[1] > 101):
            return False
        if (self.visited[current[0]][current[1]] == 1):
            return False
        return True
    
    def mark_visited(self, move):
        x,y = move
        self.visited[x][y] = True
    
    def Manhattan(x,y, goalX, goalY):
        return math.sqrt((abs(x - goalX)**2) + (abs(y - goalY)**2))
    
        
    
        
        
        