class Rectangulo:
    def __init__(self, base, altura, color = "sin color"):
        self.base = base
        self.altura = altura
        self.color = color

    def area(self):
        return self.base * self.altura
    def perimetro(self):
        return 2 * (self.base + self.altura)
    def __str__(self):
        return (f"Rectángulo de base {self.base}, altura {self.altura}, color {self.color}, área {self.area()} y perímetro {self.perimetro()}")

base = int(input("Ingrese la base del rectángulo: "))
altura = int(input("Ingrese la altura del rectángulo: "))
color = input("Ingrese el color del rectángulo: ")
if base > 0 and altura > 0:
    f1 = Rectangulo(base, altura, color)
    print(f1)
else:
    print("Error: La base y la altura deben ser mayores que 0.")
