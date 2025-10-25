from datetime import datetime # libreia para manejar fechas
from Cuenta import Cuenta
class CuentaJoven(Cuenta):
    def __init__(self, titular, saldo=0, bonificacion=0, fecha_nacimiento="01/01/2000"):
        super().__init__(titular, saldo)
        self.__bonificacion = bonificacion
        self.__fecha_nacimiento = fecha_nacimiento

    def getBonificacion(self):
        return self.__bonificacion

    def getFechaNacimiento(self):
        return self.__fecha_nacimiento

    def setBonificacion(self, bonificacion):
        self.__bonificacion = bonificacion

    def setFechaNacimiento(self, fecha_nacimiento):
        self.__fecha_nacimiento = fecha_nacimiento

    def calcularEdad(self, fecha_nacimiento):
        fecha_nac = datetime.strptime(fecha_nacimiento, "%d/%m/%Y")            # Convertir la cadena de fecha a un objeto datetime https://www.analyticsvidhya.com/blog/2024/01/python-datetime-strptime-function/
        hoy = datetime.now()
        edad = hoy.year - fecha_nac.year - ((hoy.month, hoy.day) < (fecha_nac.month, fecha_nac.day))
        return edad

    def esTitularValido(self, edad):
        if edad is None:
            return False
        if 18 <= edad < 25:
            return True
        elif edad < 18:
            print("El titular es menor de edad")
            return False
        else:
            print("El titular es mayor de 25 años")
            return False
    def retirar(self, monto, edad):
        if monto <= 0:
            print("El monto a retirar debe ser positivo")
        elif monto > 500:
            print("El monto a retirar excede el límite permitido")
        else:
            super().retirar(monto)

if __name__ == "__main__":
    Titular = input("Ingrese el nombre del titular de la cuenta joven: ")
    FechaNacimiento = input("Ingrese la fecha de nacimiento del titular (dd/mm/yyyy): ")
    cuenta_joven = CuentaJoven(Titular, fecha_nacimiento=FechaNacimiento)
    edad = cuenta_joven.calcularEdad(FechaNacimiento)
    if not cuenta_joven.esTitularValido(edad):
        print("Programa finalizado: el titular no cumple con los requisitos de edad (18-24 años).")
        exit()
    print("Titular válido. Bienvenido a tu Cuenta Joven.")
    while True:
        print("------Operaciones Cuenta Joven------")
        print("1. Mostrar información de la cuenta joven")
        print("2. Ingresar dinero")
        print("3. Retirar dinero")
        print("4. Salir")
        opcion = input("Seleccione una opción (1-4): ")
        
        if opcion == '1':
            cuenta_joven.mostrar()
            print(f"Bonificación: {cuenta_joven.getBonificacion()}%, Fecha de Nacimiento: {cuenta_joven.getFechaNacimiento()}, Edad: {edad}")
        elif opcion == '2':
            monto = float(input("Ingrese el monto a ingresar: "))
            cuenta_joven.ingresar(monto)
        elif opcion == '3':
            monto = float(input("Ingrese el monto a retirar: "))
            cuenta_joven.retirar(monto, edad)
        elif opcion == '4':
            break