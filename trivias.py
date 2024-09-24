"""lista_compras = []

while True:
    item = input("Ingrese un artículo para agregar a la lista (o 'salir' para terminar): ")
    if item == 'salir':
    else: 
        break 
    lista_compras.append(item)

print("Lista de compras:")
for i in range(lista_compras):
    print("- " + lista_compras[i])"""



"""  
class Circulo:
    def __init__(radio):
        self.radio = radio

    def calcular_area(self):
        return 3.14159 * radio ** 2 #La formula matematica es Pi por Radio al cuadrado el "** 2" es cuadrado.

mi_circulo = Circulo(5)
print(f"El área del círculo es: mi_circulo.calcular_area()")"""


"""cadena = "Hola Mundo"
vocales = "aeiou"
contador = 0

for letra in cadena:
    if letra.lower in vocales:
        contador + 1

print("Número de vocales en la cadena:  {contador}")"""

"""class Personas:
    def __init__(self, nombre, edad, profesion):
        self.nombre= nombre
        self.edad = edad
        self.profesion = profesion
    def datos(self):
        print(f"la persona {self.nombre}{self.edad}{self.profesion}")
    def mayor(self):
        if self >= 18: 


        self <=18
gaspar= Personas ("Gaspar",25,"Profesor")
diego = Personas ("Diego",45, "Desarrollador de software")
pamela= Personas ("Pamela", 36, "Estudiante")"""


class Persona:
    def __init__ (self, nombre , edad, profesion):
        self.nombre = nombre
        self.edad = edad
        self.profesion = profesion
        
    def datos (self):
        print(f"la persona{self.nombre},{self.edad},{self.profesion}")

    
        if  es_mayor_de_edad(self) :
            if self.edad >=18:
                return("Usted es mayor de edad")
        else:
                return("Usted es menor de edad")

persona_1 = Persona("Diego",45,"Desarrollador de software")
persona_2 = Persona("Gaspar",23,"Profesor")
persona_3 = Persona("Pamela",36,"Estudiante")

persona_1.imprimir()
persona_2.imprimir()
persona_3.imprimir()

print(persona_1.es_mayor_de_edad())
print(persona_2.es_mayor_de_edad())
print(persona_3.es_mayor_de_edad())