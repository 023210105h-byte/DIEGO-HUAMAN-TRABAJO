class Calculadora:
    @staticmethod
    def sumar(a, b):
        return a + b

    @staticmethod
    def restar(a, b):
        return a - b

    @staticmethod
    def multiplicar(a, b):
        return a * b

    @staticmethod
    def dividir(a, b):
        if b == 0:
            return "Error: división por cero"
        return a / b

if __name__ == "__main__":
    print("Uso desde la clase:")
    print("Suma:", Calculadora.sumar(10, 5))
    print("Resta:", Calculadora.restar(10, 5))
    print("Multiplicación:", Calculadora.multiplicar(10, 5))
    print("División:", Calculadora.dividir(10, 5))
    print("División por cero:", Calculadora.dividir(10, 0))

    print("\nUso desde una instancia:")
    calc = Calculadora()
    print("Suma:", calc.sumar(3, 7))
    print("Resta:", calc.restar(20, 8))
    print("Multiplicación:", calc.multiplicar(6, 4))
    print("División:", calc.dividir(15, 3))
