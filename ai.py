

import random




memory = []
greetings = ['hola', 'hello', 'hi','hey!','Hello','Hi']
questions = ['How are you?','How are you doing?', 'How you been?']
responses = ['Okay','I am fine','good!','That is awesome!']
validations = ['yes','yeah','yea','no','No','Nah','nah']
verifications = ['Are you sure?','You sure?','you sure?','sure?',"Sure?"]

while True:


	userInput = raw_input("Test ")
	if userInput in greetings:
		random_greetings = random.choice(greetings)
		print(random_greetings)
	elif userInput in questions:
		random_responses = random.choice(responses)
		print(random_responses)
	elif userInput in validations:
		random_verifications = random.choice(verifications)
		print(random_verifications)
	else:
		print("I did not understand what you said.")

#'''This can be extended with elif statements and eventually you will eventually
# have your very own slightly clever AI. Just make sure that the else statement
#is always at the bottom of your code'''
