#The X problem
x=0
y=0
#the actual x
Xy=0
total=0
while (y <=100):
    x=0

    while (x<=100):
        total=total+1
        if x==y:
            print(total)
            print(x,y,total)
            if y==100-x:
                print('Part of X')
                Xy=Xy+1
            Xy=Xy+1
        x=x+10
    print (y)
    y=y+10
print (total,Xy)    


