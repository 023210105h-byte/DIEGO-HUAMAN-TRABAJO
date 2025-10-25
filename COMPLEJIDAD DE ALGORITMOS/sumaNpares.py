import time
def sumaNpares(n):
    suma = 0
    for i in range(0, 2 * n, 2):
        suma += i
    return suma

def medir_tiempo_ejecucion(n):
    start_time = time.time()
    resultado = sumaNpares(n)
    end_time = time.time()
    tiempo_transcurrido = end_time - start_time
    print(f"Resultado sumaNpares({n}) = {resultado}")
    print(f"Tiempo de ejecución: {tiempo_transcurrido:.6f} segundos")
    return tiempo_transcurrido
# Ejemplo de uso
n = 10
medir_tiempo_ejecucion(n)