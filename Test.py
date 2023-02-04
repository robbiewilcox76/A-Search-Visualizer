from AStar import AStar
from MinHeap import MinHeap
from Maze import Maze
import math
import random

##file used to test min heap, give it a try and make sure it works - Robbie

x = Maze()
visited = []
for i in range(101):
    lvl = []
    for j in range(101):
        lvl.append(0)
    visited.append(lvl)

## Test AStar
AStar.execute((x.startX, x.startY), (x.targetX, x.targetY), x, visited)
