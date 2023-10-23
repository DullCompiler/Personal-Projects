#counting loop
total=0
counter=0
y=0
while (y <= 100000):
    x=0
   
    while (x <= 100000):
        total=total+1
        if (y*y+x*x)**.5>100000:
            counter=counter+1
#        print(x,y,counter,(y*y+x*x)**.5)
        x=x+10
    print (y)
    y=y+10
#print (total,counter)
print (4*(total-counter)/total)







