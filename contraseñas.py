"""Realizar un login que permita ingresar con varios usuarios y contraseñas"""

listaUsuarios = ["Pamela","Diego","Mateo"]
listaPassword = ["27Pi12Lar","Diego123","Alma2024"]

Usuario1= "Pamela"
Password1= "27Pi12Lar"
    
Usuario2= "Diego"
Password2= "Diego123"

Usuario3= "Mateo"
Password3= "Alma2024"


passcorrecta = False

while passcorrecta == False:
    ingrese_usuario = input("ingrese el usuario a continuacion:")
    ingrese_pass = input("ingrese la contraseña a continuacion:")
    for i in range(len(listaUsuarios)):
        if listaUsuarios[i] == ingrese_usuario and listaPassword[i] == ingrese_pass:
            print("Bienvenido usuario")
            passcorrecta = True
        else:
            print("Contraseña incorrecta")  






















