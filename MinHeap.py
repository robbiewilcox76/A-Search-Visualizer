import math
class MinHeap:
    def __init__(self):
        self.arr = [((-1,-1),0)]

    def addNum(self, move, num):
        self.arr.append((move, num))
        self.swim(len(self.arr)-1)
        return

    def pop(self):
        num = self.arr[len(self.arr) - 1]
        self.arr[len(self.arr) - 1] = self.arr[1]
        self.arr[1] = num
        returnNum = self.arr.pop(len(self.arr) - 1)
        self.sink(1)
        return returnNum

    def sink(self, index):
        while index*2 < len(self.arr) and self.arr[index][1] > self.arr[index*2][1]:
            num = self.arr[index]
            if index*2 + 1 >= len(self.arr) or self.arr[index*2][1] < self.arr[index*2 + 1][1]:
                self.arr[index] = self.arr[index*2]
                self.arr[index*2] = num
                index = index*2
            else: 
                self.arr[index] = self.arr[index*2 + 1]
                self.arr[index*2 + 1] = num
                index = index*2 + 1
        return

    def swim(self, index):
        while self.arr[index][1] < self.arr[int(math.floor(index/2))][1]:
            num = self.arr[index]
            self.arr[index] = self.arr[int(math.floor(index/2))]
            self.arr[int(math.floor(index/2))] = num
            index = int(math.floor(index/2))
        return
    
    def isEmpty(self):
        return len(self.arr)
    
    def find(self, move):
        for i in range(len(arr)):
            if move == arr[i][0]:
                return i
        return False
    
    def update(self, index, value):
        if value < arr[index][1]:
            arr[index][1] = value
        self.swim(index)
        
