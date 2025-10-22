class Semaforo:
    def __init__(self, luz='rojo'):
        self.luz = luz

    def cambiar(self):
        if self.luz == 'rojo':
            self.luz = 'verde'
        elif self.luz == 'verde':
            self.luz = 'amarillo'
        else:
            self.luz = 'rojo'

    def __str__(self):
        return f"Semáforo en {self.luz.upper()}"
    
if __name__ == "__main__":
    s1 = Semaforo('rojo')
    s2 = Semaforo('verde')
    s3 = Semaforo('amarillo')

    print("Estado inicial:")
    print("S1:", s1)
    print("S2:", s2)
    print("S3:", s3)
    s1.cambiar()
    print("\nDespués de cambiar solo s1:")
    print("S1:", s1)
    print("S2:", s2)
    print("S3:", s3)
