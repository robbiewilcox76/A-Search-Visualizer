import math
class MinHeap:
    def __init__(self):
        self.arr = [0]

    def addNum(self, num):
        self.arr.append(num)
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
        while index*2 < len(self.arr) and self.arr[index] > self.arr[index*2]:
            num = self.arr[index]
            if index*2 + 1 >= len(self.arr) or self.arr[index*2] < self.arr[index*2 + 1]:
                self.arr[index] = self.arr[index*2]
                self.arr[index*2] = num
                index = index*2
            else: 
                self.arr[index] = self.arr[index*2 + 1]
                self.arr[index*2 + 1] = num
                index = index*2 + 1
        return

    def swim(self, index):
        while self.arr[index] < self.arr[int(math.floor(index/2))]:
            num = self.arr[index]
            self.arr[index] = self.arr[int(math.floor(index/2))]
            self.arr[int(math.floor(index/2))] = num
            index = int(math.floor(index/2))
        return
