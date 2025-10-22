import random

class Persona:
    def __init__(self, dni, nombre="", edad=0, sexo='H', peso=0, altura=0):
        if edad < 0:
            edad = 0
        if sexo not in ('H', 'M'):
            sexo = 'H'
        self._dni = dni
        self._nombre = nombre
        self._edad = edad
        self._sexo = sexo
        self._peso = peso
        self._altura = altura

    def get_dni(self):
        return self._dni
    def get_nombre(self):
        return self._nombre
    def get_edad(self):
        return self._edad
    def get_sexo(self):
        return self._sexo
    def get_peso(self):
        return self._peso
    def get_altura(self):
        return self._altura

    def set_dni(self, dni):
        self._dni = dni
    def set_nombre(self, nombre):
        self._nombre = nombre
    def set_edad(self, edad):
        if edad >= 0:
            self._edad = edad
        else:
            print("Error: la edad no puede ser negativa.")
    def set_sexo(self, sexo):
        if sexo in ('H', 'M'):
            self._sexo = sexo
        else:
            print("Error: el sexo debe ser H (hombre) o M (mujer).")
    def set_peso(self, peso):
        if peso >= 0:
            self._peso = peso
        else:
            print("Error: el peso no puede ser negativo.")
    def set_altura(self, altura):
        if altura > 0:
            self._altura = altura
        else:
            print("Error: la altura debe ser mayor que 0.")
    def calcular_imc(self):
        if self._altura <= 0:
            return None
        imc = self._peso / (self._altura ** 2)
        if imc < 20:
            return -1
        elif 20 <= imc <= 25:
            return 0
        else:
            return 1

    def es_mayor_de_edad(self):
        return self._edad >= 18
    def generar_dni(self):
        if not self._dni or len(str(self._dni)) != 8:
            self._dni = random.randint(10_000_000, 99_999_999)
    def __str__(self):
        return (f"Persona [DNI: {self._dni}, Nombre: {self._nombre}, Edad: {self._edad}, Sexo: {self._sexo}, Peso: {self._peso} kg, Altura: {self._altura} m]")

print("REGISTRO DE PERSONA")
dni = input("Ingrese el DNI: ")
if dni == "":
    persona = Persona(dni="")
    persona.generar_dni()
else:
    persona = Persona(dni=dni)

persona.set_nombre(input("Ingrese el nombre: "))
persona.set_edad(int(input("Ingrese la edad: ")))
persona.set_sexo(input("Ingrese el sexo (H o M): ").upper())
persona.set_peso(float(input("Ingrese el peso en kg: ")))
persona.set_altura(float(input("Ingrese la altura en metros: ")))

print("DATOS DE LA PERSONA")
print(persona)

resultado_imc = persona.calcular_imc()
if resultado_imc == -1:
    print("IMC: Bajo peso")
elif resultado_imc == 0:
    print("IMC: Peso ideal")
elif resultado_imc == 1:
    print("IMC: Sobrepeso")
else:
    print("No se pudo calcular el IMC la altura inválida.")

if persona.es_mayor_de_edad():
    print("La persona es mayor de edad.")
else:
    print("La persona es menor de edad.")