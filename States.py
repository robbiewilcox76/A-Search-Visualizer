from Maze import Maze
from enum import Enum

class Direction(Enum):
    UP = (0, 1)
    DOWN = (0, -1)
    LEFT = (-1, 0)
    RIGHT = (1, 0)

import math
class StateTree():
    def __init__(self, maze: Maze, x, y, goalX, goalY: int, parent: StateTree):
        self.current = maze
        self.x = x
        self.y = y
        self.goalX = goalX
        self.goalY = goalY
        self.parent = parent
        self.g = sys.maxsize
        self.h = Manhattan(x, y, goalX, goalY)
        self.search = 0
    
    def apply_operations(direction):
        if (direction == Direction.UP):
            return StateTree(current, x + Direction['UP'][0], y + Direction['UP'][1], goalX, goalY, self)
        else: 
            if (direction == Direction.DOWN):
                return StateTree(current, x + Direction['DOWN'][0], y + Direction['DOWN'][1], goalX, goalY, self)
            else:
                if (direction == Direction.LEFT):
                    return StateTree(current, x + Direction['LEFT'][0], y + Direction['LEFT'][1], goalX, goalY, self) 
                else:
                    return StateTree(current, x + Direction['RIGHT'][0], y + Direction['RIGHT'][1], goalX, goalY, self)
                
    def apply_valid_operations():
        states = []
        for data in Direction:
            newState = apply_operations(data.value)
            if (newState.is_valid()):
                states.append(newState)
        
        return states
    
    def is_valid():
        if (x < 0 | x > 101):
            return False
        if (y < 0 | y > 101):
            return False
        if (current[x][y] == 1):
            return False
        return True
            
    def Manhattan(x,y, goalX, goalY):
        return math.sqrt((abs(x - goalX)**2) + (abs(y - goalY)**2))
    
        
    
        
        
        