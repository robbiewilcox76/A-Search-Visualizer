from States import States
from MinHeap import MinHeap
from Maze import Maze
class AStar:
    
    @staticmethod
    def execute(initial, goal, maze, visited):
        current = initial  #current spot
        heap = MinHeap() # heap for expansion
        heap.addNum(current, 0, initial) #add current move to heap
        counter = 0
        moves = [] #array to backtrack when solution is found
        while(not heap.isEmpty()):
            current = heap.pop() #pick least expensive move
            if current[0] == goal:
                AStar.addPath(moves, maze, initial)
                maze.print_maze()
                return
            moves.append(current) #save move
            visited[current[0][0]][current[0][1]] = 1 #mark as visited
            counter += 1
            AStar.expand(visited, current, maze, heap, counter) #expand from spot
        print("No solution bozo.") #no solution if heap is empty
            

    #looks complicated but all it does is add nodes that arent blocked to heap with f(n) and changes characters so they print in red
    @staticmethod
    def expand(visited, current, maze, heap, counter): 
        if current[0][0]-1 > 0:
            if visited[current[0][0]-1][current[0][1]] != 1 and maze.grid[current[0][0]-1][current[0][1]] != 1:
                heap.addNum((current[0][0]-1, current[0][1]), maze.manhattans[current[0][0]-1][current[0][1]] + 1, (current[0][0], current[0][1]))
                if maze.grid[current[0][0]-1][current[0][1]] != 3:
                    maze.grid[current[0][0]-1][current[0][1]] = '*'

        if current[0][1]-1 > 0:
            if visited[current[0][0]][current[0][1]-1] != 1 and maze.grid[current[0][0]][current[0][1]-1] != 1:
                heap.addNum((current[0][0], current[0][1]-1), maze.manhattans[current[0][0]][current[0][1]-1] + 1, (current[0][0], current[0][1]))
                if maze.grid[current[0][0]][current[0][1]-1] != 3:
                    maze.grid[current[0][0]][current[0][1]-1] = '*'

        if current[0][0]+1 < 101:
            if visited[current[0][0]+1][current[0][1]] != 1 and maze.grid[current[0][0]+1][current[0][1]] != 1:
                heap.addNum((current[0][0]+1, current[0][1]), maze.manhattans[current[0][0]+1][current[0][1]] + 1, (current[0][0], current[0][1]))
                if maze.grid[current[0][0]+1][current[0][1]] != 3:
                    maze.grid[current[0][0]+1][current[0][1]] = '*'

        if current[0][1]+1 < 101:
            if visited[current[0][0]][current[0][1]+1] != 1 and maze.grid[current[0][0]][current[0][1]+1] != 1:
                heap.addNum((current[0][0], current[0][1]+1), maze.manhattans[current[0][0]][current[0][1]+1] + 1, (current[0][0], current[0][1]))
                if maze.grid[current[0][0]][current[0][1]+1] != 3:
                    maze.grid[current[0][0]][current[0][1]+1] = '*'

    #should print real shortest path in green, might be kind of off
    @staticmethod
    def addPath(moves, maze, initial):
        i = len(moves)-1
        index = i
        curMove = moves[0]
        while i > 0:
            curMove = moves[i]
            maze.grid[moves[i][0][0]][moves[i][0][1]] = "@"
            if curMove[0] == initial:
                return
            print(curMove)
            for j in reversed(range(i)):
                if moves[j][0] == curMove[2]:
                    curMove = moves[j]
                    i = j
                    print(i)
                    break

