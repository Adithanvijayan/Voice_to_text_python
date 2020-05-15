import speech_recognition as sr
from googletrans import Translator

r = sr.Recognizer()

translator = Translator()

with sr.Microphone() as source:
	print("SAY Something")
	audio = r.listen(source)
	print("Thanks")

try:
	text = r.recognize_google(audio)
	print("Text: "+ text)
	translation = translator.translate(text)
	print(translation.origin, ' -> ', translation.text)
except:
	pass;