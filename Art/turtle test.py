from turtle import *
a = 1
for x in range(10000):
    a=a+1
    width(x / a)
    forward(x)
    left(a)
    print(a)
    speed(100)
    
