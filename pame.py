import pyttsx3
engine = pyttsx3.init()
que_queres_que_diga= input("escribe lo que quieres que diga")
engine.say(que_queres_que_diga)

voices = engine.getProperty('voices')
for voz in voices:
     print(f"el nombre es:{voz.name}")
engine.setProperty("voice", voices[1].id)
engine.say(que_queres_que_diga)

engine.runAndWait()
