from RepeatedAStar import RepeatedAStar
from AdaptiveAStar import AdaptiveAStar
from AStar import AStar
from MinHeap import MinHeap
from Maze import Maze
from Node import Node

heap = MinHeap()
heap.addNode(Node((0,0), None, 5, 3))
heap.addNode(Node((0,1), None, 2, 1))
heap.addNode(Node((0,4), None, 4, 3))
heap.addNode(Node((0,2), None, 8, 5))
heap.addNode(Node((1,5), None, 4, 2))
heap.addNode(Node((2,1), None, 8, 1))
heap.addNode(Node((4,1), None, 8, 3))

for i in range(7):
    x = heap.pop()
    print(x)