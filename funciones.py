#Funcion para validar texto
 
def validar_texto (texto_imput:str/None="Ingrese un texto:")-> str:
    while True:
     texto = input ("Ingrese un texto:")
     if not texto.isdigit():
        break
     else:
         print("Ingrese un texto valido")
    return texto


texto_imprimir=validar_texto("Ingrese su nombre y apellido")
print (f"el texto ingresado es:{texto_imprimir}")

