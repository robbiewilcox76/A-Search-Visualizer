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


# AStar.execute([x.startX, x.startY], [x.targetX, x.targetY], x, visited)
heap = MinHeap()
# heap.addNode(Node((0,0), None, 2, 0))
# heap.addNode(Node((0,2), None, 7, 0))
# heap.addNode(Node((1,2), None, 4, 0))
# heap.addNode(Node((4,2), None, 2, 0))
# heap.addNode(Node((2,2), None, 9, 0))
# heap.addNode(Node((7,2), None, 3, 0))
# heap.addNode(Node((2,4), None, 5, 0))

heap.addNode(Node((0,0), None, 8, 0))
heap.addNode(Node((0,2), None, 7, 0))
heap.addNode(Node((1,2), None, 6, 0))
heap.addNode(Node((4,2), None, 5, 0))
heap.addNode(Node((2,2), None, 4, 0))
heap.addNode(Node((7,2), None, 3, 0))
heap.addNode(Node((2,4), None, 2, 0))

print("[")
for i in range(1, len(heap.arr)):
    print(heap.arr[i].total_cost)
print("]")
#print([0, 1] == [0, 1])