"""
Nombre y Apellido: Pamela Izaguirre
Edad: 36
DNI:33581419
Email: pameiza88@gmail.com
"""

#Objetivo del ejercicio: Arreglar los siguientes programas con errores:

#Ejercicio 1: Saludar usuario. 
#Cantidad errores: 3
nombre_usuario = input( "Ingrese su nombre")
print(f"Hola, {nombre_usuario} Bienvenido!")


#Ejercicio 2: Promedio de 4 numeros. 
#Cantidad errores: 5
num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
num3 = int(input("Ingrese el tercer número: "))
num4 = int(input("ingrese el cuarto numero:"))
promedio =( num1 + num2 + num3 + num4 )/ 4
print(f"El promedio es: {promedio}")

#Ejercicio 3: Verificar si el estudiante aprobo:
#Cantidad de errores: 3

calificacion = int(input("Ingrese la calificación del estudiante: "))
texto = "El estudiante ha aprobado"
if calificacion >= 6:
    print(texto)
else:
    texto= "El estudiante ha reprobado"
    print(texto)

#Ejercicio 4: Lista de Compras.
#Cantidad de errores: 1
lista_compras = []

while True:
    item = input("Ingrese un artículo para agregar a la lista (o 'salir' para terminar): ")
    if item == 'salir':
        break
    lista_compras.append(item)

print("Lista de compras:")
for i in range(len(lista_compras)):
    print("- " + lista_compras[i])

#Ejercicio 5: Clase Circulo.
#Cantidad de errores: 5

class Circulo:
    def __init__(self,radio:int):
        self.radio = radio

    def calcular_area(self):
        area = 3.14159 *(self.radio ** 2) #La formula matematica es Pi por Radio al cuadrado el "** 2" es cuadrado.
        return area
Mi_circulo = Circulo(5)
print(f"El área del círculo es: {mi_circulo.calcular_area()}")


#Ejercicio 6: Generar un numero Aleatorio.
#Cantidad de errores: 3
import random
numero = random.randit(1, 10)
print(f"El número aleatorio generado es:{ numero}")

#Ejercicio 7: Contar Vocales en una Cadena:
#Cantidad errores: 4

cadena = "Hola Mundo"
vocales = "aeiou"
contador = 0

for letra in cadena:
    if letra.lower() in vocales:
        contador + 1

print(f"Número de vocales en la cadena:  {contador}")

#Ejercicio 8: Funcion para repetir cadenas.
#Cantidad de errores: 3
def repetir_cadena(cadena, veces):
    resultado = cadena * veces
    return resultado

texto = input("Ingrese un texto: ")
repeticiones = int(input("¿Cuántas veces desea repetir el texto? "))
print(f"El texto repetido es: {repetir_cadena(texto,repeticiones)}")

#Ejercicio 9: Crear una clase llamada Persona.
#Crea tres instancias de la clase persona:
# Gaspar, 23, Profesor.
# Diego, 45, Desarrollador de Software.
# Tu nombre, tu edad, tu profesion.
# Crea metodos para imprimir el nombre, la edad y la profesion de cada persona.
# Crea un metodo para saber si la persona es mayor o menor de edad.

class Personas:
    def __init__(self, nombre, edad, profesion):
        self.nombre= nombre
        self.edad = edad
        self.profecion = profesion
    def datos (self):
            print(f"la persona {self.nombre},{self.edad},{self.profesion}")
    def mayor_menor(self):
        if self.edad >= 18:
                print: ("usted es mayor de edad")
        else: 
                print:("usted es menor de edad")

gaspar= Personas ("Gaspar",25,"Profesor")
diego= Personas ("Diego",45, "Desarrollador de software")
pamela= Personas ("Pamela", 36, "Estudiante")#Ejercicio 2: Promedio de 4 numeros. 
#Cantidad errores: 5
num1 = int(input("Ingrese el primer numero:"))
num2 = int(input("Ingrese el segundo numero:"))
num3 =int(input("Ingrese el tercer numero:"))
num4=int(input("ingrese el cuarto numero:"))

promedio = num1 + num2 + num3 + num4 / 4
print(f"El promedio es: {promedio}")
