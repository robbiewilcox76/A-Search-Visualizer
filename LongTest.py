from RepeatedAStar import RepeatedAStar
from AStar import AStar
from MinHeap import MinHeap
from Maze import Maze
from Node import Node
import math
import random


##file used to test min heap, give it a try and make sure it works - Robbie

maze_size = 100
x = Maze(maze_size)
visited = []
for i in range(x.height):
    lvl = []
    for j in range(x.height):
        lvl.append(0)
    visited.append(lvl)

## Test RepeatedAStar

find = RepeatedAStar([x.startX, x.startY], [x.targetX, x.targetY], x, maze_size)
find.execute()