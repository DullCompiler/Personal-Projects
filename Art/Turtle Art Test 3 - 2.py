from turtle import *
a=0.05
colors = ['red', 'purple', 'blue', 'green', 'yellow', 'orange']
for i in range(1000000):
    width(6+a)
    pencolor(colors[i % 6])
    forward(i)
    left(81)
    speed(1000000000000000000000000)
    a=a+0.1
    
    
    
    
          
