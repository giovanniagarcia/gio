import turtle
myturtle = turtle.turtle()
myturtle.shape("turtle")


prevNum = 0
currNum = 1
nextNum = prevNum + currNum
number_of_terms = 15
myturtle.color(`red`)
for i in range (number_of_terms):


     #draw a sqiral
     print(currNum)
     for f in range (currNum - prevNum):
        myturtle.right(360/currNum)
        myturtle.forward(10)


     #fibonacci calculation
     nextNum = currNum + prevNum
     prevNum = currNum
     currNum = nextNum
        
