l#crea una funcion q nos salude la consola

def saludar(nombre):
  print(f"Hola {nombre},¿Como estas?")
saludar("Pame")


#crea una funcion paracalcular el area de un cuadrado

def area_cuadrado(lado):
         area = lado * lado
         return area
cuadrado = int(input("ingrese el valor del lado:"))
area= area_cuadrado(cuadrado)
print(f"el area del cuadrado es igual:{area}")





#crea una funcion para ordenar una lista de palabras

lista_palabras=["gato","perro","casa","auto", "jengibre"]
lista_palabras_2=["gato","perro", "jengibre"]
lista_palabras_3=["casa","auto", "jengibre"]
def ordenar_palabras(listas):
        listas.sort()
        return listas


print(ordenar_palabras(lista_palabras))
print(ordenar_palabras(lista_palabras_3))
print(ordenar_palabras(lista_palabras_2))

#crea una funcion para verificar si un numero es par o impar

def es_par_o_impar (numero:)
numero=int(input("ingrese un numero"))
resultado = es_par_o_impar(numero)
print(resuntado)
return el numero es_par_o_impar

#crea una funcion de encontrar maximo y min entre 3 numero 

