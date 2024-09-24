import pyttsx3

engine = pyttsx3.init()
que_queres_que_diga= input("escribe lo que quieras que diga")
rate = engine.getProperty('rate')
print(f"la velocidad actual es{rate}")
engine.setProperty('rate', 150)
engine.say(que_queres_que_diga)
engine.setProperty('rate', 50)
engine.say(que_queres_que_diga) 

engine.runAndWait()
 