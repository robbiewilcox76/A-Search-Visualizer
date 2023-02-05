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
        for i in range(103):
            print("-", end = "")
        print("")
        
        for i in range(101):
            if i < 10: print("{}    |".format(i), end = "")
            else: 
                if(i >= 100): print("{}  |".format(i), end = "")
                else: print("{}   |".format(i), end = "")
            for j in range(101):
                if self.grid[i][j] == 1:
                    print("#", end = "")
                else: 
                    if self.grid[i][j] == 0:
                        print(" ", end = "")
                    else: 
                        if self.grid[i][j] == 2:
                            self.prCyan("S")
                        else:
                            if self.grid[i][j] == '*':
                                self.prRed("*")
                            else:
                                if self.grid[i][j] == '@':
                                    self.prGreen("*")
                                else:
                                    self.prCyan("T")
            print("|")
        print("     ", end = "")
        for i in range(103):
            print("-", end = "")
        print("")

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

        self.grid[self.startX][self.startY] = 2 #Start = 2
        self.grid[self.targetX][self.targetY] = 3 #Target = 3

        for i in range(1, 100):
            for j in range(1, 100):
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
        for i in range(101):
            lev = []
            for j in range(101):
                lev.append(abs(i-self.targetX) + abs(j-self.targetY))
            self.manhattans.append(lev)
        
        self.perceivedMap = []
        for i in range(101):
            lev = []
            for j in range(101):
                lev.append(0)
            self.perceivedMap.append(lev)
    
        self.print_maze()
