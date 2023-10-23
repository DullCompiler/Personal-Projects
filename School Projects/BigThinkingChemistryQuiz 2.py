import time
print("Welcome, To The Big Thinking Project Quiz.")
time.sleep(3)
print("Today We Are Studying 8F.")
time.sleep(3)
print("The Instructions Are Simple, There Will Be A Question and 3 Letters Corresponding To Answers (ie. a, b and c).")
print("Type The Answer You Think is Correct.")
score=0
correct=0
wrong=0

time.sleep(10)
##Q1
print("Question One")
print("What is oxidisation?")
print("a When a Substance combines with Air (Oxygen).")
print("b When a Substance Becomes Air")
print("c When a Substance Makes Air")
answer=input()
if answer == "a":
	correct=correct+1
	print("Well Done, That Was Correct!")
else:
	print("That Was Wrong, The Answer was when a substance combines with air (oxygen).")
	wrong=wrong+1
	
##Q2
print("Question Two")
print("What Does Cl Stand For?")
print("a Calcium")
print("b Chlorine")
print("c Copper")
answer=input()
if answer =="b":
	correct=correct+1
	print("Well Done, That Was Correct!")
else:
	print("That Was Wrong, The Answer was Chlorine.")
	wrong=wrong+1
	
##Q3
print("Question Three")
print("What is the PH Range?")
print("a 0 - 10")
print("b 1 - 15")
print("c 0 - 14")
answer=input()
if answer =="c":
	correct=correct+1
	print("Well Done, That Was Correct!")
else:
	print("That Was Wrong, The Answer was 0 - 14.")
	wrong=wrong+1
	
##Q4
print("Question Four")
print("What is the Scientific Name for Water")
print("a H2o")
print("b H20")
print("c Water-oxide.")
answer=input()
if answer =="a":
	correct=correct+1
	print("Well Done, That Was Correct!")
else:
	print("That Was Wrong, The Answer was H2o.")
	wrong=wrong+1
	
##Q5
print("Question Five")
print("What is a property of a Noble Gas?")
print("a Red")
print("b Reacts with H2o")
print("c Extremly UnReactive")
answer=input()
if answer =="c":
	correct=correct+1
	print("Well Done, That Was Correct!")
else:
	print("That Was Wrong, The Answer was Extremly UnReactive.")
	wrong=wrong+1
	
##Q6
print("Question Six")
print("How many groups in the periodic table?")
print("a 18")
print("b 15")
print("c 20")
answer=input()
if answer =="a":
	correct=correct+1
	print("Well Done, That Was Correct!")
else:
	print("That Was Wrong, The Answer was 18.")
	wrong=wrong+1
	
##Q7
print("Question Seven")
print("Who Invented the Periodic Table?")
print("a Bill Nye")
print("b Dmitri Mendeleev")
print("c Ernest Runtherford")
answer=input()
if answer =="b":
	correct=correct+1
	print("Well Done, That Was Correct!")
else:
	print("That Was Wrong, The Answer was Dmitri Mendeev.")
	wrong=wrong+1
	
##Q8
print("Question Eight")
print("Why Are Alkali Metals Covered In Oil")
print("a It's Very Reactive")
print("b It Looks Good")
print("c It stops bacteria from destroying the material")
answer=input()
if answer =="a":
	correct=correct+1
	print("Well Done, That Was Correct!")
else:
	print("That Was Wrong, The Answer was It's Very Reactive.")
	wrong=wrong+1
	
print("Well done")
print("Correct")
print(correct)
print("Wrong")
print(wrong)
print("Thank You For Playing")
