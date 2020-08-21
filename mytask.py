import pyttsx3
import os

pyttsx3.speak("Welcome Anusha I am here to help you")
print("Welcome Anusha I am here to help you")

while True:
	print("Tell me Anusha what can I do for you :"  , end='')
	p = input()

	if (("don't "in p) or ("dont "in p) or ("do not "in p) or ("no need to" in p) ) and ( ("run" in p)  or ("chrome" in p) or ("browser" in p)):
		pyttsx3.speak("OK Anusha")	
		print("OK Anusha")	

	elif (("run" in p) or  ("execute" in p ) or ("open" in p)) and  (("chrome" in p) or ("browser" in p) ) :
		pyttsx3.speak("Here I am opening chrome browser for You")
		os.system("start chrome")

	elif (("don't "in p) or ("dont "in p) or ("do not "in p) or ("no need to" in p) ) and ( ("run" in p)  or ("media" in p) or ("player" in p)):
		pyttsx3.speak("OK Anusha")	
		print("OK Anusha")	

	elif (("run" in p) or  ("execute" in p ) or ("open" in p)) and  (("media" in p) or ("player" in p) ) :
		pyttsx3.speak("Here I am opening windows media player for You")
		os.system("start wmplayer")

	elif (("don't "in p) or ("dont "in p) or ("do not "in p) or ("no need to" in p) ) and ( ("run" in p)  or ("editor" in p) or ("notepad" in p)):
		pyttsx3.speak("OK Anusha")	
		print("OK Anusha")

	elif (("run" in p) or  ("execute" in p ) or ("open" in p)) and  (("editor" in p) or ("notepad" in p) ) :
		pyttsx3.speak("Here I am opening editor notepad for You")
		os.system("start notepad")

	elif(("QUIT" in p) or("quit" in p) or("Quit" in p) or ("EXIT" in p) or ("exit" in p) or ("Exit" in p)):
		break

	else:
		#pyttsx3.speak("wrong input")
		print("hey sorry ..Anusha ,can you please enter correct task")
	



