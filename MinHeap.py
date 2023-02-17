import math
from Node import Node
class MinHeap:
    mode = 1 # default mode: choosing smaller g value
    
    def __init__(self):
        self.arr = [Node([-1, -1], None, -1, -1)]
        self.smaller_tie_break = 1
        self.bigger_tie_break = 2
        self.const = 110 # constant c larger than any possible g value

    def addNode(self, node: Node):
        idx = self.find(node)
        if idx>0:
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
        
        while index*2 < len(self.arr):
            child = index * 2 # child on left node
            if (child + 1 < len(self.arr) and 
                (self.arr[child+1].total_cost < self.arr[child].total_cost 
                 or self.special_smaller(self.arr[child+1], self.arr[child])
                 )):
                child += 1 #choose child on right node
            
            if ((self.arr[index].total_cost < self.arr[child].total_cost) 
                or self.special_smaller(self.arr[index], self.arr[child])
                ):
                break
            num = self.arr[index]
            self.arr[index] = self.arr[child]
            self.arr[child] = num
            index = child
        return

    def swim(self, index):
        while (self.arr[index].total_cost < self.arr[index//2].total_cost
               or self.special_smaller(self.arr[index], self.arr[index//2])
               ):
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
       return -1
    
    def update(self, index, node):
        if node.total_cost < self.arr[index].total_cost:
           self.arr[index] = node
           self.swim(index)
        return
    
    def special_smaller(self, a, b):
        if (self.mode == self.smaller_tie_break):
            return (a.total_cost == b.total_cost and a.step_cost < b.step_cost)
        else:
            a_cost = self.const * a.total_cost - a.step_cost
            b_cost = self.const * b.total_cost - b.step_cost
            return (a.total_cost == b.total_cost and a_cost < b_cost)
            
            

    def toString(self):
        print("[")
        for i in range(1, len(self.arr)):
            print(self.arr[i].total_cost)
        print("]")
        return