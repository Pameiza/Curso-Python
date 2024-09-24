class Cuenta_Bancaria:
    def __init__(self,titular,saldo_inicial=0):
        self.titular=titular
        self.saldo=saldo_inicial
        def deposito(self,monto):
            if monto >0:
                if monto <= self.saldo:
                    self.saldo -= monto
                print(f"Has retirado {monto} unidades. saldo actual:{self.saldo}")
            else:
                print("Tienes fondos insuficientes para realizar la operacion")
def consultar_saldo(self):
    print(f"saldo actual-,{self.saldo}unidades")

    titular=input("Ingrese el nombre del titular:")
    caja_ahorro=Cuenta_Bancaria(Pamela, 0)

while True:
     opcion = input("Elije la opcion que quieres realizar:\n-Depositar (D) \n-Retirar(R)\n-Mostrar Saldo (S)\n-Si quieres finalizar sesion (F) \n-Opcion:").upper()
     if opcion == "D" or opcion == "R" or opcion == "S" or opcion == "F":
        if opcion == "D":
            cuenta_bancaria.depositar()
        if opcion == "R":
            cuenta_bancaria.retirar()
        if opcion == "S":
            cuenta_bancaria.mostrar_saldo()
        if opcion == "F":
            cuenta_bancaria.mostrar_saldo()
        exit("Finalizando Sesion con Exito")
     else:
        print("Ingresaste una opcion incorrecta (D,R,S,F)")
        print("\n"*10)

