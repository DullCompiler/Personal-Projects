#The graph problem
x=0
y=0
#the actual x
Xy=0
total=0
x=0
while (x<=1000):
    if x/20 == int(x/20):
        Xy=Xy+1
        if int(x/20)==2*x:
            Xy=Xy-1
    x=x+10

x=0
while (y<=1000):
    Xy=Xy+1
    x=x+10
    y=2*x
  

    print(x,Xy)




