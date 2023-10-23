QS=0
loop=0
def begin():
	(_)
QS1A="Tod is very happy!"
QS1B="tod is very Happy!."
QS2A="i like chocolate hot dogs and ballons"
QS2B="I like chocolate, hotdogs and ballons."
QS3A="Apple is a very succsessful company."
QS3B="apple is a very scsesfl company"
if input()=="password":
	print("Setup")
	print("Select the question set that you want")
	print("Type Q1 for question set one")
	print("Type Q2 for question set two")
	print("Type Q3 for question set two")
while loop==0:
	if loop==1:
		begin:
	if input()=='Q1':
		QS==1
		print("Question Set 1 Selected")
		loop==loop+1
	if input()=='Q2':
		QS==2 
		print("Question Set 2 Selected")
		loop==loop+1
	if input()=='Q3':
		QS==3
		print("Question Set 3 Selected")	
		loop==loop+1

