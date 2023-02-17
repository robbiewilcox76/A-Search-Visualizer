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
x.reverse()

adaptForward = AdaptiveAStar([x.startX, x.startY], [x.targetX, x.targetY], x, maze_size)
# repeatForward = RepeatedAStar([x.startX, x.startY], [x.targetX, x.targetY], x, maze_size)

# repeatForward.execute(x)
# reFor += RepeatedAStar.expandedNodes
# AStar.expandedNodes = 0
# RepeatedAStar.expandedNodes = 0
AdaptiveAStar.expandedNodes = 0

#AStar.pathReset(x)
adaptForward.execute(x.manhattans, x)