import random
from turtle import *

for i in range(500):
    
    numberfrwrd=random.randint(1,100)
    numberleft=random.randint(1,360)
    numberright=random.randint(1,360)
    numberwidth=random.randint(1,10)
    numberdecide=random.randint(1,2)

    forward(numberfrwrd)
    if numberdecide==2:
        left(numberleft)
    else:
        right(numberright)
    speed(5)
    width(numberwidth)