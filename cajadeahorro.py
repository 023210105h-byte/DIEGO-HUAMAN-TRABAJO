class Cuenta:
    def __init__(self, saldo_inicial=0):
        self._saldo = saldo_inicial
        if self._saldo < 0:
            raise ValueError("El saldo inicial no puede ser negativo.")
    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, valor):
        if valor >= 0:
            self._saldo = valor
        else:
            raise ValueError("El saldo no puede ser negativo.")

    def depositar(self, monto):
        if monto > 0:
            self._saldo += monto
        else:
            raise ValueError("El monto a depositar debe ser positivo.")

    def retirar(self, monto):
        if monto <= 0:
            raise ValueError("El monto a retirar debe ser positivo.")
        elif monto > self._saldo:
            raise ValueError("Fondos insuficientes.")
        else:
            self._saldo -= monto

    def __str__(self):
        return f"Cuenta con saldo actual: S/ {self._saldo:.2f}"


if __name__ == "__main__":
    print("Bienvenido a tu caja de ahorro")
    saldo_inicial = float(input("Ingresa tu saldo inicial: "))
    cuenta = Cuenta(saldo_inicial)
    while True:
        print("\n--- MENÚ ---")
        print("1. Consultar saldo")
        print("2. Depositar dinero")
        print("3. Retirar dinero")
        print("4. Salir")
        opcion = input("Elige una opción: ")
        try:
            if opcion == "1":
                print(cuenta)

            elif opcion == "2":
                monto = float(input("Monto a depositar: "))
                cuenta.depositar(monto)
                print("Depósito exitoso.")

            elif opcion == "3":
                monto = float(input("Monto a retirar: "))
                cuenta.retirar(monto)
                print("Retiro exitoso.")

            elif opcion == "4":
                print("Gracias por usar tu caja de ahorro.")
                break

            else:
                print("Opción inválida, intenta nuevamente.")
        except ValueError as e:
            print("Error:", e)
