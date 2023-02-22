from RepeatedAStar import RepeatedAStar
from AdaptiveAStar import AdaptiveAStar
from AStar import AStar
from MinHeap import MinHeap
from Maze import Maze
from Node import Node

smallerCount = 0
biggerCount = 0
ran = 50
# for i in range(ran):
#     AStar.expandedNodes = 0
#     maze_size = 101
#     x = Maze(maze_size)
#     startManhattan = x.manhattans
#     visited = []
#     for i in range(x.height):
#         lvl = []
#         for j in range(x.height):
#             lvl.append(0)
#         visited.append(lvl)

#     # Adaptive using smaller g value tie breaker
#     MinHeap.mode = 1
#     RepeatedAStar.expandedNodes = 0
#     a = RepeatedAStar([x.startX, x.startY], [x.targetX, x.targetY], x, maze_size)
#     a.execute(x)
#     smallerCount += RepeatedAStar.expandedNodes
#     RepeatedAStar.expandedNodes = 0
    

#     # Adaptive using bigger g value tie break
#     MinHeap.mode = 2
#     RepeatedAStar.expandedNodes = 0
#     b = RepeatedAStar([x.startX, x.startY], [x.targetX, x.targetY], x, maze_size)
#     b.execute(x)
#     biggerCount += RepeatedAStar.expandedNodes
#     RepeatedAStar.expandedNodes = 0
    
        
# print("Repeated using smaller g value tie breaker")
# print("Nodes expanded: {}".format(smallerCount/50))
# print("Repeated using bigger g value tie break")
# print("Nodes expanded: {}".format(biggerCount/50))

AStar.expandedNodes = 0
maze_size = 20
x = Maze(maze_size)
x.empty_maze([0, 0], [19,19])

# Adaptive using smaller g value tie breaker
MinHeap.mode = 1
RepeatedAStar.expandedNodes = 0
print("Repeated using smaller g value tie breaker")
a = RepeatedAStar([x.startX, x.startY], [x.targetX, x.targetY], x, maze_size)
a.execute(x)
smallerCount += RepeatedAStar.expandedNodes
RepeatedAStar.expandedNodes = 0


# Adaptive using bigger g value tie break
MinHeap.mode = 2
RepeatedAStar.expandedNodes = 0
b = RepeatedAStar([x.startX, x.startY], [x.targetX, x.targetY], x, maze_size)
print("Repeated using bigger g value tie break")
b.execute(x)
RepeatedAStar.expandedNodes = 0

