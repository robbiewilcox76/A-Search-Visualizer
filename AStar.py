from States import States
from MinHeap import MinHeap
from Maze import Maze
class AStar:
    
    @staticmethod
    def execute(initial, goal, maze, visited):
        current = initial
        heap = MinHeap()
        heap.addNum(current, 0)
        counter = 0
        print(current)
        moves = []
        while(not heap.isEmpty()):
            current = heap.pop() 
            if current[0] == goal:
                AStar.addPath(moves, maze)
                maze.print_maze()
                break
            if counter != 0:
                moves.append(current)
            visited[current[0][0]][current[0][1]] = 1
            counter += 1
            AStar.expand(visited, current, maze, heap, counter)
            

    @staticmethod
    def expand(visited, current, maze, heap, counter):
        if current[0][0]-1 > 0:
            if visited[current[0][0]-1][current[0][1]] != 1 and maze.grid[current[0][0]-1][current[0][1]] != 1:
                heap.addNum((current[0][0]-1, current[0][1]), maze.manhattans[current[0][0]-1][current[0][1]] + 1)
                if maze.grid[current[0][0]-1][current[0][1]] != 3:
                    maze.grid[current[0][0]-1][current[0][1]] = '*'

        if current[0][1]-1 > 0:
            if visited[current[0][0]][current[0][1]-1] != 1 and maze.grid[current[0][0]][current[0][1]-1] != 1:
                heap.addNum((current[0][0], current[0][1]-1), maze.manhattans[current[0][0]][current[0][1]-1] + 1)
                if maze.grid[current[0][0]][current[0][1]-1] != 3:
                    maze.grid[current[0][0]][current[0][1]-1] = '*'

        if current[0][0]+1 < 101:
            if visited[current[0][0]+1][current[0][1]] != 1 and maze.grid[current[0][0]+1][current[0][1]] != 1:
                heap.addNum((current[0][0]+1, current[0][1]), maze.manhattans[current[0][0]+1][current[0][1]] + 1)
                if maze.grid[current[0][0]+1][current[0][1]] != 3:
                    maze.grid[current[0][0]+1][current[0][1]] = '*'

        if current[0][1]+1 < 101:
            if visited[current[0][0]][current[0][1]+1] != 1 and maze.grid[current[0][0]][current[0][1]+1] != 1:
                heap.addNum((current[0][0], current[0][1]+1), maze.manhattans[current[0][0]][current[0][1]+1] + 1)
                if maze.grid[current[0][0]][current[0][1]+1] != 3:
                    maze.grid[current[0][0]][current[0][1]+1] = '*'

    @staticmethod
    def addPath(moves, maze):
        for i in range(len(moves)):
            maze.grid[moves[i][0][0]][moves[i][0][1]] = "@"
