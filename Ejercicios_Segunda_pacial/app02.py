import pyttsx3

engine = pyttsx3.init()
engine.say("Dame tu nombre")
engine.runAndWait()
name = input("Dame tu nombre ")
engine.say(f"Hola {name}")
engine.runAndWait()