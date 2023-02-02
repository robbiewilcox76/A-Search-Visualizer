from MinHeap import MinHeap

##file used to test min heap, give it a try and make sure it works - Robbie

x = MinHeap()
x.addNum(1.76)
x.addNum(3.245)
x.addNum(4.1324)
x.addNum(1.7)
x.addNum(1.72)
x.addNum(0.11)
print(x.arr)
while len(x.arr) > 1:
    y = x.pop()
    print("popped {}".format(y))
