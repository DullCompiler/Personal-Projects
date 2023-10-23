#player_registration
import time


#registration subroutine
def registration():
    print("To register please enter the following information")
    print("What is your first name?")
    first_name=input()
    print("what is your last name?")
    last_name=input()
    print("please enter your nickname")
    nick_name=input()
    print("please enter your email address")
    email=input()
    print("what is your skill level? c(asual) or e(xpert)")
    skill=input()
    if skill=="c":
        skill="casual"
    if skill=="e":
        skill="expert"
    print("is this information correct")
    print("name = ",first_name," ",last_name,", nickname: ",nick_name,", email: ",email," skill level = ", skill)
    print("is that correct? y or n")
    answer=input()
    if answer=="y":
        print("Registration confirmed, thank you")
    if answer=="n":
        registration()
#startup
print("Hello and welcome to the FireSide Gaming Tournament. Do you want to apply? y or n?")
if input()=="y":
    registration()


    
