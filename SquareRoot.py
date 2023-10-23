stop=0
print("Enter a number to find it's sqaure root")
numfrsq=input()
numfrsq=float(numfrsq)
print("original input = ",numfrsq)

difference=1
hi=float(numfrsq)
low=float(0)
mid=float((hi+low)/2)
print("high: ", hi)
print("middle point: ", mid)
print("low: ", low)

while difference>=0.0001:
    #too high
    while mid*mid>numfrsq:
        hi=mid  
        mid=(hi-low)/2+low
        difference=float((mid*mid-numfrsq)**2)
        print("difference: ", difference)
        print("mid**2: ", mid**2)
        print("high: ", hi)
        print("middle point: ", mid)
        print("low: ", low)
        
    #too low    
    while mid*mid<numfrsq:
        low=mid
        mid=(hi-low)/2+low
        difference=float((mid*mid-numfrsq)**2)
        print("difference: ", difference)
        print("mid**2: ", mid**2)
        print("high: ", hi)
        print("middle point: ", mid)
        print("low: ", low)

print("Program Complete")
print("Square root of ", numfrsq, " is ", mid)