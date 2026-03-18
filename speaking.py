import pyttsx3

engine_object = pyttsx3.init()

engine_object.setProperty('rate', 150)

engine_object.setProperty('voice', 'f4')
#
# pdf = 'CAT_MEMORY.pdf'
# engine_object.say(pdf)

engine_object.say("Hello World, my name is Abiton. Very enthusiatic about developing modern technologies.")

engine_object.runAndWait() #call to the function
