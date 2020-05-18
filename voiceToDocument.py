import speech_recognition as sr
from docx import Document
import random

document = Document()

pdf_text = ""
text = ""

while 1:
	r = sr.Recognizer()
	with sr.Microphone() as source:
		print("SAY Something")
		audio = r.listen(source)
		print("Thanks")

	try:
		text = r.recognize_google(audio)
		if text == "stop":
			break
		print("Text: "+ text)
		text = text + " "
		pdf_text = pdf_text + text
	except:
		pass;

document.add_paragraph(pdf_text)
print("Paragraph : "+pdf_text)
print("Document created successfully")
fileName = 'demo'+str(random.randint(1,1000))+'.docx'
document.save(fileName)