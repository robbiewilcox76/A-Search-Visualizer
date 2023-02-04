from AStar import AStar
from MinHeap import MinHeap
from Maze import Maze
import math
import random

##file used to test min heap, give it a try and make sure it works - Robbie

x = Maze()

## test Heap
heap = MinHeap()
heap.addNum((1,1), 3)
heap.addNum((2,3), 2)
heap.addNum((4,2), 9)
heap.addNum((2,2), 5)
#print(heap.arr)

#while len(heap.arr) > 1:
#    y = heap.pop()
#    print("popped {} move".format(y[1]), y[0])
    

## Test AStar
#a = AStar((x.startX, x.startY), (x.targetX, x.targetY), x).execute()
maze = Maze()
maze.printMaze()