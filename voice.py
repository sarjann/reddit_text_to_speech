import pyttsx3

engine = pyttsx3.init()

""" RATE"""
rate = engine.getProperty('rate')   # getting details of current speaking rate
engine.setProperty('rate', 180)     # setting up new voice rate


"""VOLUME"""
volume = engine.getProperty('volume')   #getting to know current volume level (min=0 and max=1)
engine.setProperty('volume',1.0)    # setting up volume level  between 0 and 1

"""VOICE"""
voices = engine.getProperty('voices')       #getting details of current voice

engine.setProperty('voice', voices[7].id)

def speak(msg):
	engine.say(msg)
	engine.runAndWait()
	engine.stop()
