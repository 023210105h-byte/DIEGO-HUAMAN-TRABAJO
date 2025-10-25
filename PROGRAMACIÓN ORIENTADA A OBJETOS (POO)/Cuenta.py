class Cuenta:
    def __init__(self, titular, saldo=0):
        self.__titular = titular
        self.__saldo = saldo
    
    def getTitular(self):
        return self.__titular
    
    def getSaldo(self):
        return self.__saldo
    
    def setTitular(self, titular):
        self.__titular = titular
        
    def setSaldo(self, saldo):
        self.__saldo = saldo
    
    def mostrar(self):
        print(f"Titular: {self.__titular}, Saldo: {self.__saldo}")
        
    def ingresar(self, monto):
        if monto <= 0:
            print("El monto a ingresar debe ser positivo")
        elif monto > 1000:
            print("El monto a ingresar excede el límite permitido")
        else:
            self.__saldo += monto
            print(f"Monto ingresado: {monto}. Nuevo saldo: {self.__saldo}")
            
    def retirar(self, monto):
        if monto <= 0:
            print("El monto a retirar debe ser positivo")
        elif monto > 1000:
            print("El monto a retirar excede el límite permitido")
        elif monto > self.__saldo:
            print("Fondos insuficientes para realizar el retiro")
        else:
            self.__saldo -= monto
            print(f"Monto retirado: {monto}. Nuevo saldo: {self.__saldo}")
    
if __name__ == "__main__":
    Titular = input("Ingrese el nombre del titular de la cuenta: ")
    cuenta = Cuenta(Titular)
    while True:
        print("------Operaciones------")
        print("1. Mostrar información de la cuenta")
        print("2. Ingresar dinero")
        print("3. Retirar dinero")
        print("4. Salir")
        opcion = input("Seleccione una opción (1-4): ")
        
        if opcion == '1':
            cuenta.mostrar()
        elif opcion == '2':
            monto = float(input("Ingrese el monto a ingresar: "))
            cuenta.ingresar(monto)
        elif opcion == '3':
            monto = float(input("Ingrese el monto a retirar: "))
            cuenta.retirar(monto)
        elif opcion == '4':
            print("Saliendo del programa.")
            break