from RepeatedAStar import RepeatedAStar
from AdaptiveAStar import AdaptiveAStar
from AStar import AStar
from MinHeap import MinHeap
from Maze import Maze
from Node import Node
import math
import random


##file used to test min heap, give it a try and make sure it works - Robbie

aFor = 0
aBack = 0
reFor = 0
reBack = 0
ran = 10
MinHeap.mode = 2
for i in range(ran):
    AStar.expandedNodes = 0
    maze_size = 101
    x = Maze(maze_size)
    startManhattan = x.manhattans
    visited = []
    for i in range(x.height):
        lvl = []
        for j in range(x.height):
            lvl.append(0)
        visited.append(lvl)

    adaptForward = AdaptiveAStar([x.startX, x.startY], [x.targetX, x.targetY], x, maze_size)
    repeatForward = RepeatedAStar([x.startX, x.startY], [x.targetX, x.targetY], x, maze_size)

    repeatForward.execute(x)
    reFor += RepeatedAStar.expandedNodes
    AStar.expandedNodes = 0
    RepeatedAStar.expandedNodes = 0
    AdaptiveAStar.expandedNodes = 0

    #AStar.pathReset(x)
    adaptForward.execute(x.manhattans, x)
    aFor += AdaptiveAStar.expandedNodes
    AStar.expandedNodes = 0
    RepeatedAStar.expandedNodes = 0
    AdaptiveAStar.expandedNodes = 0

    #AStar.pathReset(x)
    x.manhattans = startManhattan
    x.reverse()
    adaptBackWard = AdaptiveAStar([x.startX, x.startY], [x.targetX, x.targetY], x, maze_size)
    repeatBackward = RepeatedAStar([x.startX, x.startY], [x.targetX, x.targetY], x, maze_size)

    repeatBackward.execute(x)
    reBack += RepeatedAStar.expandedNodes
    AStar.expandedNodes = 0
    RepeatedAStar.expandedNodes = 0
    AdaptiveAStar.expandedNodes = 0

    #AStar.pathReset(x)
    adaptBackWard.execute(x.manhattans,x)
    aBack += AdaptiveAStar.expandedNodes


print("Repeated forward: {}".format(reFor/ran))
print("Repeated backward: {}".format(reBack/ran))
print("Adapted forward: {}".format(aFor/ran))
print("Adapted backward: {}".format(aBack/ran))