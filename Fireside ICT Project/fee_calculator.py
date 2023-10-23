#fee_calculator
import time
skill_continue=0
origin_continue=0
fee_registration=0

#welcome
print("This is the fee calculator, this will determine the total cost foy your registration.")
time.sleep(1)
print("Are you sure you want to apply to the Fireside Tournament (y or n)")
time.sleep(1)

#y or n input var get
question=input()
if question=="n":

    #stop
    print("We're sad to see you go, hope to see you next year!")

if question=="y":

    #continue
    print("Good to hear, please answer the following questions")
    while fee_registration==0:

        #email ask
        email=input("Please enter your email ")

        #skill ask
        while skill_continue==0:
            skill=input("Please enter your skill level c(asual) or e(xpert) ")
            if skill=="c" or skill=="e":
                skill_continue=1
                if skill=="c":
                    skill="casual"
                if skill=="e":
                    skill="expert"
            else:
                print("Please enter a valid input")

        #origin ask
        while origin_continue==0:
            origin=input("Where are you registering from? 'UK', 'US' or 'AU' ")
            if origin== "UK" or origin=="US" or origin=="AU":
                origin_continue=1
            else:
                print("Please enter a valid input")

        #info confirm
        print("Email: ", email, " - Skill: ", skill, " - Country Registration: ", origin)
        time.sleep(1)
        print("Is this correct? y or n")
        if input()=="y":
            fee_registration=1

#fee calculate point

#Variables
fee_calc_reset=0
base_fee=float(10)
cas_fee=float(20)
exp_fee=float(35)
gbp_gbp=float(1.0)
usd_gbp=float(1.5)
aud_gbp=float(2.0)

#Intro  
print("The fee to join is 10 Great British Pounds (GBP)")
time.sleep(1)
print("However, there is a price increase if you are a casual or an expert")
time.sleep(5)
print("Casual Fee: 20 Great British Pounds (GBP)")
print("Expert Fee: 35 Great British Pounds (GBP)")
time.sleep(10)

#Calc Point
print("Your prior information says that you're from ", origin, " and that you're a ", skill, ".")

#UK
if origin=="UK":
    if skill=="casual":
        print("Your fee is ", ((base_fee*gbp_gbp)+(cas_fee)), " GBP")
    if skill=="expert":
        print("Your fee is ", ((base_fee*gbp_gbp)+(exp_fee)), " GBP")

#US
if origin=="US":
    if skill=="casual":
        print("Your fee is ", ((base_fee*usd_gbp)+(cas_fee)), " USD")
    if skill=="expert":
        print("Your fee is ", ((base_fee*usd_gbp)+(exp_fee)), " USD")

#AU
if origin=="AU":
    if skill=="casual":
        print("Your fee is ", ((base_fee*aud_gbp)+(cas_fee)), " AUD")
    if skill=="expert":
        print("Your fee is ", ((base_fee*aud_gbp)+(exp_fee)), " AUD")