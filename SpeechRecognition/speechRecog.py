import speech_recognition as sr
r = sr.Recognizer()
with sr.Microphone() as source:
	print("Hello")
	audio = r.listen(source)
	try:
		print("You said " + r.recognize_google(audio))
	except LookupError:
		print("Could not understand Audio")
