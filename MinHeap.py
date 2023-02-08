import math
from Node import Node
class MinHeap:
    def __init__(self):
        self.arr = [Node([0, 0], None, 0, 0)]

    def addNode(self, node: Node):
        idx = self.find(node)
        if idx:
            self.update(idx,node)
        else: 
            self.arr.append(node)
            self.swim(len(self.arr) - 1)
            return

    def pop(self):
        num = self.arr[len(self.arr) - 1]
        self.arr[len(self.arr) - 1] = self.arr[1]
        self.arr[1] = num
        returnNode = self.arr.pop(len(self.arr) - 1)
        self.sink(1)
        return returnNode

    def sink(self, index):
        #print("-------------")
        while index*2 < len(self.arr) and self.arr[index].total_cost > self.arr[index*2].total_cost:
            num = self.arr[index]
            if index*2 + 1 >= len(self.arr) or self.arr[index*2].total_cost < self.arr[index*2 + 1].total_cost:
                self.arr[index] = self.arr[index*2]
                self.arr[index*2] = num
                index = index*2
            else: 
                self.arr[index] = self.arr[index*2 + 1]
                self.arr[index*2 + 1] = num
                index = index*2 + 1
        return

    def swim(self, index):
        while index > 0 and self.arr[index].total_cost < self.arr[index//2].total_cost:
            num = self.arr[index]
            self.arr[index] = self.arr[index//2]
            self.arr[index//2] = num
            index = index//2
        return
    
    def isEmpty(self):
        return len(self.arr) == 1
    
    def find(self, node):
       for i in range(len(self.arr)):
           if node.position == self.arr[i].position:
               return i
       return False
    
    def update(self, index, node):
        if node.total_cost < self.arr[index].total_cost:
           self.arr[index] = node
           self.swim(index)
        return

    def toString(self):
        print("[")
        for i in range(1, len(self.arr)):
            print(self.arr[i].total_cost)
        print("]")
        return