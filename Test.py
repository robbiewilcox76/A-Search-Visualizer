from AStar import AStar
from MinHeap import MinHeap
from Maze import Maze
from Node import Node
import math
import random

##file used to test min heap, give it a try and make sure it works - Robbie

x = Maze(100)
visited = []
for i in range(x.height):
    lvl = []
    for j in range(x.height):
        lvl.append(0)
    visited.append(lvl)

## Test AStar


AStar.execute([x.startX, x.startY], [x.targetX, x.targetY], x, visited)

#print([0, 1] == [0, 1])