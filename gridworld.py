import random
from flask import Flask, render_template
app = Flask(__name__)
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
    targetX = random.randint(0, 100)
    targetY = random.randint(0, 100)
    startX = random.randint(0, 100)
    startY = random.randint(0, 100)
    array1[targetX][targetY]=2
    array1[startX][startY]=3
    foo=0
    for i in array1:
        fum=0
        for j in i:
            if (foo == startX and fum == startY) or (foo == targetX and fum == targetY):
                continue
            prob = random.random()
            if array1[foo-1][fum] == 1 or array1[foo][fum-1] == 1:
                if prob > .5:
                    array1[foo][fum] = 1
            else:
                if(prob > .7):
                    array1[foo][fum] = 1
            fum+=1
        foo+=1
    return render_template('gridworld.html', array=array1)
if __name__=='__main__':
    app.run(debug=True)