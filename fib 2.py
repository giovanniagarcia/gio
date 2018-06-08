import turtle
myTurtle = turtle.Turtle()
myTurtle.shape("turtle")


prevNum = 0
currNum = 1
nextNum = prevNum + currNum
fibNums = [prevNum, currNum ]
prevNum = currNum
currNum = nextNum
fibNums.append(currNum )

#draw a square
for x in fibNums:
    print(x)
    myTurtle.right(90)
    myTurtle.forward(10)
