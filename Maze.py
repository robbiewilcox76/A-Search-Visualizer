import random

class Maze:
    def __init__(self):
        self.height = 101
        self.width = 101
        self.grid = []
        for i in range(101):
            level = []
            for j in range(101):
                level.append(0)
            self.grid.append(level)

        self.targetX = random.randint(0, 100)
        self.targetY = random.randint(0, 100)
        self.startX = random.randint(0, 100)
        self.startY = random.randint(0, 100)

        self.grid[self.targetX][self.targetY] = 2 #Start = 2
        self.grid[self.startX][self.startY] = 3 #Target = 3

        for i in range(1, 101):
            for j in range(1, 101):
                if (i == self.startX and j == self.startY) or (i == self.targetX and j == self.targetY):
                    continue
                prob = random.random()
                if self.grid[i-1][j] == 1 or self.grid[i][j-1] == 1:
                    if prob > .5:
                        self.grid[i][j] = 1
                else:
                    if(prob > .7):
                        self.grid[i][j] = 1

        for i in range(101):
            print(self.grid[i])
        


