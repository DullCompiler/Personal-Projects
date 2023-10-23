#import time and random
import time
import random

#initialise the grid
line10=["[100]", "[99]", "[98]", "[97]", "[96]", "[95]", "[94]", "[93]", "[92]", "[91]"]
line9 = ["[81]", "[82]", "[83]", "[84]", "[85]", "[86]", "[87]", "[88]", "[89]", "[90]"]
line8 = ["[80]", "[79]", "[78]", "[77]", "[76]", "[75]", "[74]", "[73]", "[72]", "[71]"]
line7 = ["[61]", "[62]", "[63]", "[64]", "[65]", "[66]", "[67]", "[68]", "[69]", "[70]"]
line6 = ["[60]", "[59]", "[58]", "[57]", "[56]", "[55]", "[54]", "[53]", "[52]", "[51]"]
line5 = ["[41]", "[42]", "[43]", "[44]", "[45]", "[46]", "[47]", "[48]", "[49]", "[50]"]
line4 = ["[40]", "[39]", "[38]", "[37]", "[36]", "[35]", "[34]", "[33]", "[32]", "[31]"]
line3 = ["[21]", "[22]", "[23]", "[24]", "[25]", "[26]", "[27]", "[28]", "[29]", "[30]"]
line2 = ["[20]", "[19]", "[18]", "[17]", "[16]", "[15]", "[14]", "[13]", "[12]", "[11]"]
line1 = ["[01]", "[02]", "[03]", "[04]", "[05]", "[06]", "[07]", "[08]", "[09]", "[10]"]

#initialise the variables
die=0
die_total=0
goes=0
goes_total=0
validation_loop=0
validation=0
continue_sl=0

#print aray subrutine
def printgrid():
    print(line10)
    print(line9)
    print(line8)
    print(line7)
    print(line6)
    print(line5)
    print(line4)
    print(line3)
    print(line2)
    print(line1)

#intro
print("Welcome to Snakes and ladders")
time.sleep(0.5)
print("A virtual dice will be rolled for you")
print("Do you want to play?")
while validation_loop==0:
    validation=input("Enter valiation - y or n: ")
    if validation=="y":
        validation_loop=1
        time.sleep(1)
    if validation=="n":
        print("Hope to see you soon")
        validation_loop=1
    if validation!="y" or validation!="n":
        print("Please enter a valid input")

(line1[0])="[X]"
printgrid()
(line1[0])="[01]"

#die
die=random.randint(1,6)
die_total=die_total+1
print("The Dice rolled a ",die)

#move accross the grid
print("Counter Place updated")
if die_total<=11:
    die_total=die_total-10
    (line2[die_total])="[X]"
    printgrid
    (line2[die_total])="[",die_total,"]"
if die_total>=11:
    (line1[die_total])="[X]"
    printgrid
    (line1[die_total])="[",die_total,"]"

die=random.randint(1,6)
die_total=die_total+1
print("The Dice rolled a ",die)

print("Counter Place updated")
if die_total<=11:
    die_total=die_total-10
    (line2[die_total])="[X]"
    printgrid
    (line2[die_total])="[",die_total,"]"
if die_total>=11:
    (line1[die_total])="[X]"
    printgrid
    (line1[die_total])="[",die_total,"]"
