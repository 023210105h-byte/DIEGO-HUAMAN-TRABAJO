import math

class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

    def distancia(self, otro):
        if not isinstance(otro, Punto):
            raise TypeError("El argumento debe ser una instancia de la clase Punto.")
        dx = self.x - otro.x
        dy = self.y - otro.y
        return math.sqrt(dx**2 + dy**2)

if __name__ == "__main__":
    p1 = Punto(3, 4)
    p2 = Punto(7, 1)

    print(f"Punto 1: {p1}")
    print(f"Punto 2: {p2}")

    print(f"Distancia entre los puntos: {p1.distancia(p2):.2f}")