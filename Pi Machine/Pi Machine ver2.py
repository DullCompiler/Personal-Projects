#counting loop
total=0
counter=0
area1=5040
y=700
x=700
total=total+area1

while (y<=1000):
    x=700
    while (x<=1000):
        total=total+1
        if (y*y+x*x)**.5>1000:
            counter=counter+1
        #print(x,y,counter,total,(y*y+x*x)**.5)
        x=x+10
    #print (y)
    y=y+10
print(x,y,counter,total,(y*y+x*x)**.5)

x=710
y=0
while (y<=690):
    x=710
    while (x<=1000):
        total=total+1
        if (y*y+x*x)**.5>1000:
            counter=counter+1
        #print(x,y,counter,total,(y*y+x*x)**.5)
        x=x+10
    #print (y)
    y=y+10
print(x,y,counter,total,(y*y+x*x)**.5)

x=0
y=710
while (y<=1000):
    x=0
    while (x<=690):
        total=total+1
        if (y*y+x*x)**.5>1000:
            counter=counter+1
        #print(x,y,counter,total,(y*y+x*x)**.5)
        x=x+10
    #print (y)
    y=y+10
print(x,y,counter,total,(y*y+x*x)**.5)

print (total,counter)
print (4*(total-counter)/total)
