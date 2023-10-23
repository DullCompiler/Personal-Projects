from turtle import *
import random

screensize(360,360)
color('red', 'yellow')
begin_fill()
while True:
    forward(200)
    left(170)
    if abs(pos()) < 1:
        break

end_fill()
done()

screen.onclick(debswirl())

def debswirl():
    
    color('pink', 'purple')
    while True:
        x=1
        forward(x)
        while x <=40:
            x=x+0.25
        if x <=40:
            break
