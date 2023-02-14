from RepeatedAStar import RepeatedAStar
from AdaptiveAStar import AdaptiveAStar
from AStar import AStar
from MinHeap import MinHeap
from Maze import Maze
from Node import Node
import math
import random


##file used to test min heap, give it a try and make sure it works - Robbie
for i in range(50):
    AStar.expandedNodes = 0
    maze_size = 101
    x = Maze(maze_size)
    visited = []
    for i in range(x.height):
        lvl = []
        for j in range(x.height):
            lvl.append(0)
        visited.append(lvl)

    ## Test RepeatedAStar

    find = AdaptiveAStar([x.startX, x.startY], [x.targetX, x.targetY], x, maze_size)
    m = RepeatedAStar([x.startX, x.startY], [x.targetX, x.targetY], x, maze_size)
    #print("\n")
    #for i in range(x.height):
    #    print(x.manhattans[i])
    #
    m.execute()
    AStar.expandedNodes = 0
    find.execute(x.manhattans)
print("Adaptive: {}".format(AdaptiveAStar.expandedNodes/50))
print("Repeated: {}".format(RepeatedAStar.expandedNodes/50))