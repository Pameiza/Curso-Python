#Definiendo  OBJETOS

class Vehiculos:
        def __init__(self, color:str, marca:str, modelo:str, puertas:int):
         self.color = "rojo"
         self.puertas = 2
         self.modelo = "fiesta"
         self.marca = "ford"

        def mostrar_caracteristicas(self):
                print(f"El auto es de color ¨{self.color},Tiene puertas {self.puertas} y el modelo es {self.modelo} de la marca")
        def mostrar_color(self):
                return


auto_diego = Vehiculos("rojo",2,"Fiesta", "Ford")
auto_gaspar = Vehiculos("azul", 4, "Duster", "Renault")
auto_leti = Vehiculos("negro", 5, 208, "Peugeot")
print(f"El color es {auto_gaspar.color}")
auto_gaspar.mostrar_caracteristicas() 
auto_diego.mostrar_caracteristicas()
auto_leti.mostrar_caracteristicas()


