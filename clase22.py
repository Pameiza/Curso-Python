#Ingresa 3 numeros indicar cual es el mayor
def ingrese_un_numero():
    while True:
        numero = input("ingrese un numero:")
        if numero.isdigit():
            numero = int (numero)

            break
        else:
            print("El numero ingresado no es valido")
            numero = 0
    return numero

mayor = 0
menor = 0
suma = 0
for contador in range(3):
    numero = ingrese_un_numero()
    print(f"El {contador+1}º Nº ingresado es:{numero}")
    if numero > mayor:
        mayor=numero
        if numero < menor or menor == 0:
            menor = numero
    suma = suma + numero

print(f"El numero mayor es {mayor}")
print(f"El numero menor es {menor}")
print(f"El numero promedio es igual: {suma/3}")

