import random
import math

class Maze:

    def prCyan(self, skk): 
        print("\033[96m{}\033[00m" .format(skk), end = "")

    def prRed(self, skk): 
        print("\033[91m{}\033[00m" .format(skk), end = "")

    def prGreen(self, skk): 
        print("\033[92m{}\033[00m" .format(skk), end = "")

    def print_maze(self):
        print("     ", end = "")
        for i in range(len(self.grid)+2):
            print("-", end = "")
        print("")
        
        for i in range(len(self.grid)):
            if i < 10: print("{}    |".format(i), end = "")
            else: 
                if(i >= 100): print("{}  |".format(i), end = "")
                else: print("{}   |".format(i), end = "")
            for j in range(len(self.grid)):
                if self.grid[i][j] == 1:
                    print("#", end = "")
                else: 
                    if self.grid[i][j] == 0:
                        print(" ", end = "")
                    else: 
                        if self.grid[i][j] == 2:
                            self.prCyan("S")
                        else:
                            if self.grid[i][j] == 6:#'*':
                                self.prRed("*")
                            else:
                                if self.grid[i][j] == 5:#'@':
                                    self.prGreen("*")
                                else:
                                    self.prCyan("T")
            print("|")
        print("     ", end = "")
        for i in range(len(self.grid)+2): #103
            print("-", end = "")
        print("")

    def empty_maze(self):
        self.grid = []
        for i in range(self.width):
            level = []
            for j in range(self.width):
                level.append(0)
            self.grid.append(level)
        self.grid[self.targetX][self.targetY] = 3
        self.grid[self.startX][self.startY] = 2
        
    def empty_maze(self, initial, goal):
        self.grid = []
        for i in range(self.width):
            level = []
            for j in range(self.width):
                level.append(0)
            self.grid.append(level)
        self.grid[goal[0]][goal[1]] = 3
        self.grid[initial[0]][initial[1]] = 2
        self.startX = initial[0]
        self.startY = initial[1]
        self.targetX = goal[0]
        self.targetY = goal[1]
        
        self.manhattans = []
        for i in range(self.height): #101
            lev = []
            for j in range(self.height): #101
                lev.append(abs(i-self.targetX)+ abs(j-self.targetY))
            self.manhattans.append(lev)


    def check_walls(self, newMaze, x, y):
        if x+1 < self.width and self.grid[x+1][y] == 1:
            newMaze[x+1][y] = 1
        if y+1 > self.width and self.grid[x][y-1] == 1:
            newMaze[x][y+1] = 1
        if x-1 > 0 and self.grid[x-1][y] == 1:
            newMaze[x-1][y] = 1
        if y-1 > 0 and self.grid[x][y-1] == 1:
            newMaze[x][y-1] = 1


    def __init__(self, dimension):
        self.height = dimension #101
        self.width = dimension #101
        self.grid = []
        for i in range(self.height): #101
            level = []
            for j in range(self.height): #101
                level.append(0)
            self.grid.append(level)

        self.targetX = random.randint(0, self.height-1) #all 0, 100
        self.targetY = random.randint(0, self.height-1)
        self.startX = random.randint(0, self.height-1)
        self.startY = random.randint(0, self.height-1)

        self.grid[self.startX][self.startY] = 2 #Start = 2
        self.grid[self.targetX][self.targetY] = 3 #Target = 3

        for i in range(0, self.height): #101
            for j in range(0, self.height): #101
                if (i == self.startX and j == self.startY) or (i == self.targetX and j == self.targetY):
                    continue
                prob = random.random()
                if self.grid[i-1][j] == 1 or self.grid[i][j-1] == 1:
                    if prob > .6:
                        self.grid[i][j] = 1
                else:
                    if(prob > .8):
                        self.grid[i][j] = 1

        self.manhattans = []
        for i in range(self.height): #101
            lev = []
            for j in range(self.height): #101
                lev.append(abs(i-self.targetX) + abs(j-self.targetY))
            self.manhattans.append(lev)
        self.reverseManhattans=[]
        # for i in range(self.height): #101
        #     lev = []
        #     for j in range(self.height): #101
        #         lev.append(abs(i-self.startX) + abs(j-self.startY))
        #     self.manhattans.append(lev)
        self.perceivedMap = []
        for i in range(self.height): #101
            lev = []
            for j in range(self.height): #101
                lev.append(0)
            self.perceivedMap.append(lev)
    
    def walkable(self, x, y):
        if (x >= 0 and x < self.width and y>=0 and y < self.height):
            return self.grid[x][y] != 1
        else: return False
    
    def reverse(self):
        x=self.startX
        self.startX=self.targetX
        self.targetX=x
        x=self.startY
        self.startY=self.targetY
        self.targetY=x
        self.reverseManhattans=self.manhattans
        self.manhattans = []
        self.grid[self.startX][self.startY] = 2 #Start = 2
        self.grid[self.targetX][self.targetY] = 3 #Target = 3
        for i in range(self.height): #101
            lev = []
            for j in range(self.height): #101
                lev.append(abs(i-self.targetX) + abs(j-self.targetY))
            self.manhattans.append(lev)
