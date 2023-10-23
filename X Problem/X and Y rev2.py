#The X problem
x=0
y=0
#the actual x
Xy=0
total=0
while (y <=1000):
    x=0
    while (x<=1000):
        total=total+1
        if y==2*x:
            Xy=Xy+1
            print('Part of X')
            if y==x/2:
                Xy=Xy-1
        if y==x/2:
            print('Part of X')
            Xy=Xy+1
        x=x+10
        print(x,y,Xy,total)
    y=y+10
print (total,Xy)    


