from AStar import AStar
from MinHeap import MinHeap
from Maze import Maze
from Node import Node
from RepeatedAStar import RepeatedAStar
import math
import random


##file used to test min heap, give it a try and make sure it works - Robbie

def ReversePath(node: Node):
    ptr = node
    prev = None
    while ptr != None:
        next = ptr.parent
        ptr.parent = prev
        prev = ptr
        ptr = next
    return prev

x = Maze(10)
visited = []
for i in range(x.height):
    lvl = []
    for j in range(x.height):
        lvl.append(0)
    visited.append(lvl)

## Test AStar

vanilla_total = 0
forward_repeated_total = 0
for i in range(1):
    x = Maze(10)
    visited = []
    for i in range(x.height):
        lvl = []
        for j in range(x.height):
            lvl.append(0)
        visited.append(lvl)
    x.reverse()
    moves = AStar.execute([x.startX, x.startY], [x.targetX, x.targetY], x, visited)
    x.print_maze()
    visited = []
    for i in range(x.height):
        lvl = []
        for j in range(x.height):
            lvl.append(0)
        visited.append(lvl)
    vanilla_total += AStar.expandedNodes
    AStar.expandedNodes = 0
    forward_repeated_total += RepeatedAStar.expandedNodes
for node in AStar.expandedArr:
    print(node.position)
print("Forward: {}\n Repeated: {}".format(vanilla_total, forward_repeated_total/50))
