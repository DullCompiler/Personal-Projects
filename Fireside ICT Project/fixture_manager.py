#fixture manager

#Imports
import sys

#variables
loop=0
always_on_loop=0

#command set
print("Fixture Manager V0.8")
#(^ update each version)
print("Enter either 'A', 'B', 'C' or 'Q'")
print("Option A: Search for a fixture")
print("Option B: Outstanding fixtures")
print("Option C: Display Leader Board")
print("Enter Q to quit")

#get option choice
while loop==0:
    option=input("enter option choice: ")
    if option=='A' or option=='B' or option=='C' or option=='Q':
        loop=1

#Exit
if option =='Q':
    print("got it, quit")
    sys.exit()

#Option A
if option =='A':
    print("got it option A")

#Option B
if option =='B':
    print("got it option A")

#Option C
if option =='C':
    print("got it option A")



