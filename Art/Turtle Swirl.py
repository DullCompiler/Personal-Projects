# import packages
import turtle
import random

t=turtle.Pen()
t.speed(100)
colors=['red', 'yellow', 'green', 'purple', 'blue', 'orange']

# set screen
sc = turtle.Screen()
sc.setup(10000, 10000)
turtle.bgcolor("black")
  
# start pattern creation
for x in range(15):
    randomamount=random.randint(60,200)
    print(randomamount)
    for x in range(randomamount):
        t.pencolor(colors[x%6]) # setting color
        t.width(x/100 + 1) # setting width
        t.forward(x) # moving forward
        t.left(59) # moving left