import random
from flask import Flask, render_template, request
from Maze import Maze
app = Flask(__name__)
maze=Maze(101)
@staticmethod
@app.route("/path")
def reload(grid):
    print("nay")
    return render_template('gridworld.html', array=grid)
@app.route("/")
def main():
    # x=0
    array1=[]
    for i in range(101):
        # if i%5==1:
        #     array2=[1 for i in range(101)]
        # else:
        array2=[0 for i in range(101)]
        array1.append(array2)
    # while x<101*101:
    #     array1
    #     x+=1
        # for array2 in array1:
        #     k=""
        #     for i in array2:
        #         k=str(k+str(i)+" ") 
            # print(k)
    #targetX = random.randint(0, 100)
    #targetY = random.randint(0, 100)
    #startX = random.randint(0, 100)
    #startY = random.randint(0, 100)
    #array1[targetX][targetY]=2
    #array1[startX][startY]=3
    #foo=0
   # for i in array1:
    #   for j in i:
     #       if (foo == startX and fum == startY) or (foo == targetX and fum == targetY):
      #          continue
       #     prob = random.random()
        #    if array1[foo-1][fum] == 1 or array1[foo][fum-1] == 1:
         #       if prob > .5:
          #          array1[foo][fum] = 1
           # else:
            #    if(prob > .7):
             #       array1[foo][fum] = 1
            #fum+=1
        #foo+=1

    global maze
    maze = Maze(101)    
    return render_template('gridworld.html', array=maze.grid)
@app.route("/AStar")
# def reload(grid):
#     print("yay")
#     render_template('gridworld.html', array=grid)
#     return
def AStar():
    from AStar import AStar
    global maze
    x=maze
    AStar.pathReset(x)
    visited=[]
    for i in range(101):
        lvl = []
        for j in range(101):
            lvl.append(0)
        visited.append(lvl)
    AStar.execute([x.startX, x.startY], [x.targetX, x.targetY], x, visited)
    print(x.startX)
    print(" ")
    print(x.startY)
    return render_template('gridworld.html', array=x.grid)
# @app.route("/staysame")
# def stay():
#     global maze
#     x=maze
#     from AStar import AStar
#     AStar.pathReset(x)
#     print(x.grid)
#     return render_template('gridworld.html', array=x.grid)
@app.route("/ReverseA*")
def reverse():
    from AStar import AStar
    global maze
    x=maze
    AStar.pathReset(x)
    Maze.reverse(x)
    visited=[]
    for i in range(101):
        lvl = []
        for j in range(101):
            lvl.append(0)
        visited.append(lvl)
    AStar.execute([x.startX, x.startY], [x.targetX, x.targetY], x, visited)
    Maze.reverse(x)
    print(x.startX)
    print(" ")
    print(x.startY)
    return render_template('gridworld.html', array=x.grid)
@app.route("/adaptiveA*")
def adapt():
    from AdaptiveAStar import AdaptiveAStar
    from AStar import AStar
    global maze
    x=maze
    AStar.pathReset(x)
    # visited=[]
    # for i in range(101):
    #     lvl = []
    #     for j in range(101):
    #         lvl.append(0)
    #     visited.append(lvl)
    astar=AdaptiveAStar([x.startX, x.startY], [x.targetX, x.targetY], x, 101)
    AdaptiveAStar.execute(astar, x.manhattans, x)
    print(AdaptiveAStar.expandedNodes)
    AdaptiveAStar.expandedNodes=0
    # print(x.startX)
    # print(" ")
    # print(x.startY)
    return render_template('gridworld.html', array=x.grid)
@app.route("/repeatedAStar")
def repeat():
    from RepeatedAStar import RepeatedAStar
    from AStar import AStar
    global maze
    x=maze
    AStar.pathReset(x)
    astar=RepeatedAStar([x.startX, x.startY], [x.targetX, x.targetY], x, 101)
    RepeatedAStar.execute(astar, x)
    print(RepeatedAStar.expandedNodes)
    RepeatedAStar.expandedNodes=0
    return render_template('gridworld.html', array=x.grid)
if __name__=='__main__':
    app.run(debug=True)