#Square Root Program Re-try
squareRinp=0
answer=0

print("Enter an input to find it's sqaure root")

#Input check
input_loop=0
while input_loop==0:
    sqaureRinp=(input("Enter valid input (A float or interger): "))
    if str(sqaureRinp).isdigit()==True:
        input_loop=1
    else:
        print("Please enter a valid input")

#takes input makes a float
sqaureRinp=float(sqaureRinp)
print(sqaureRinp)
#past input test
print("Passed Input selection True")

#Easy half number = sqr
halftest=float(sqaureRinp/2)
halftest_und=float(halftest**2)
if halftest_und==halftest**2:
    print("The squareroot is ", halftest)

#Initilasation of initial variables
high=squareRinp
mid=squareRinp/2
low=0

UH=((high-mid)/2)+(high/2)
LH=((high-mid)/2)

while (UH*UH)!=squareRinp or (LH*LH)!=squareRinp:
    #UH and LH initiliase
    UH=((high-mid)/2)+(high/2)
    LH=((high-mid)/2)

    #too high
    if (UH*UH)>=(LH*LH):
        mid=((high-mid)/2)-high
        high=mid
        low=0

    #too low
    if (UH*UH)<=(LH*LH):
        low=mid
        high=high
        mid=((high-mid)/2)-high

if UH**2==squareRinp:
    print(UH, " is the squareroot of ", squareRinp)
if LH**2==squareRinp:
    print(LH, " is the sqaureroot of ", squareRinp)
