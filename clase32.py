"""class Contador:
    def __init__(self) -> None:
    self.cuenta = 0
    pass #no es obligatorio el pass
    def incrementar (self):
        self.cuenta += 1
        return
    def decrementar(self):
        if self.cuenta > 0:
            self.cuenta -=1
            print("no se puede restar")
        return
    def mostrar_contador(self):
        print(f"el valor de contador es:{self.cuenta}")
        return
    def reiniciar(self):
        self.cuenta = 0
        return

cuenta = Contador()
cuenta.mostrar_contador()
cuenta.incrementar()
cuenta.incrementar()
cuenta.mostrar_contador()
cuenta.decrementar()
cuenta.mostrar_contador()"""

#Objetivo: Crear una clase llamada Producto 
# que tenga tres atributos: nombre, precio y cantidad. 
# Y tenga 3 metodos, Actualizar Precio, Actualizar Cantidad y Calcular valor total, 
#el primero modificara el precio del producto,
# el segundo la cantidad 
# y el ultimo debera multiplicar la cantidad por el precio del producto seleccionado para saber el valor total del inventario. 

class Producto:
    def __init__ (self, nombre, precio, cantidad) -> None:
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad
        pass
    def actualizar_precio(self,precio):
        self.precio = precio
        return
    def actualizar_cantidad(self,cantidad):
        self.cantidad = cantidad
        return
    def calcular_valor_total(self):
        return self.cantidad*self.precio
    


producto_vino = Producto("Vino", 500, 10)

print(f"nombre:{producto_vino.nombre},precio:{producto_vino.precio}, cantidad:{producto_vino.cantidad}")
producto_vino.actualizar_precio(600)
producto_vino.actualizar_cantidad(15)

print(f"valor total del inventario:{producto_vino.calcular_valor_total()} ")