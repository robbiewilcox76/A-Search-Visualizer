from AStar import AStar
from MinHeap import MinHeap
from Maze import Maze
from Node import Node
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

x = Maze(100)
visited = []
for i in range(x.height):
    lvl = []
    for j in range(x.height):
        lvl.append(0)
    visited.append(lvl)

## Test AStar


AStar.execute([x.startX, x.startY], [x.targetX, x.targetY], x, visited)
x.print_maze()
x = Node([0, 0], None, 19, 3)
y = Node([0, 1], x, 12, 3)
z = Node([0, 2], y, 21, 3)
w = Node([0, 3], z, 20, 3)
t = Node([0, 4], w, 19, 3)
u = Node([0, 5], t, 19, 3)


ptr = u
while ptr != None:
    print(ptr.position)
    ptr = ptr.parent
nodee = ReversePath(u)
print("")
ptr = nodee
while ptr != None:
    print(ptr.position)
    ptr = ptr.parent
