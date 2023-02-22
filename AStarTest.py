from RepeatedAStar import RepeatedAStar
from AdaptiveAStar import AdaptiveAStar
from AStar import AStar
from MinHeap import MinHeap
from Maze import Maze
from Node import Node

AStar.expandedNodes = 0
maze_size = 101
x = Maze(maze_size)
visited = []
for i in range(x.height):
    lvl = []
    for j in range(x.height):
        lvl.append(0)
    visited.append(lvl)

x.print_maze()

MinHeap.mode = 2

# Repeat A*
# repeatForward = RepeatedAStar([x.startX, x.startY], [x.targetX, x.targetY], x, maze_size)
# repeatForward.execute(x)
# AStar.expandedNodes = 0
# RepeatedAStar.expandedNodes = 0

# Adaptive A*
adaptForward = AdaptiveAStar([x.startX, x.startY], [x.targetX, x.targetY], x, maze_size)
AdaptiveAStar.expandedNodes = 0

AStar.pathReset(x)
adaptForward.execute(x.manhattans, x)