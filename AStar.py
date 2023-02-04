from States import States
from MinHeap import MinHeap
class AStar:
    ## each initial, goal should be passed as a pair
    def __init__(self, initial, goal, maze):
        self.initial = initial
        self.goal = goal
        self.maze = maze
        self.states = States(maze, initial, goal)
    def execute(self):
        current = self.initial
        heap = MinHeap()
        heap.addNum(current, 0)
        counter = -1
        while(not heap.isEmpty()):
            current = heap.pop() ## move object to current point
            self.states.mark_visited(current)
            counter += 1
            possibleMoves = self.states.expand(current) ## -> return a list of pairs that I can go
            for move in possibleMoves:
                f_value = counter ## cost from initial to current
                f_value += 1 ## cost from current to move
                f_value += self.maze.manhattans ## heuristic cost from move to goal
                find_index = heap.find(move)
                if find_index:
                    heap.update(move, find_index, f_value)
                else:
                    heap.addNum(move, f_value)
        
            
            
            
            
            

            
            
        
        
                    