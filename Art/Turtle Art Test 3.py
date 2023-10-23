from turtle import *
colors = ['red', 'purple', 'blue', 'green', 'yellow', 'orange']
for i in range(1000000):
    width(3)
    pencolor(colors[i % 6])
    forward(i)
    left(91)
    speed(10000000)
    
          
