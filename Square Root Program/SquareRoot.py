origin=input()
origin=float(origin)
high=origin
low=0
print(high)
print(low)
print(origin)

def pinpoint():
    print("pinpoint is working")
    highb=high*high/2
    highb=float(low)
    higha=high*high
    print("pinpoint end")

def yesno():
    #print((d*d-origin)*(d*d-origin)<1), "d")
    if (d*d-origin)*(d*d-origin)<0.001:
        print(d)
        print("yesno is working")
        print("The square root generator is close to your number, it is off by one. so far the number given by the genrator is", d)
        print(d*d, "currently this is the output of your answer")
        print("Do you want to continue? yes or no")
        if 'yes'==input():
            c=c/2
            pinpoint()
        if 'no'==input():
            print(d)

if origin==high*high:
    print(origin)
else:
    print("sec1/4 working")
    pinpoint()
    c=(high-low)/2+low
    print(c, "c")
    print(high, "high")
    print(low, "low")
    print("sec2/4 working")
    high=c/2
    print(c, "c")
    print(high, "high")
    print(low, "low")
    pinpoint()
    print("sec3/4 working")
    low=c
    high=c*2
    d=(high-low)/2
    print(c, "c")
    print(d, "d")
    print(high, "high")
    print(low, "low")
    print("sec4/4 working")
    yesno()
