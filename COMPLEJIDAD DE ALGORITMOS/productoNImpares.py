import time
def productoNImpares(n):
    producto = 1
    for i in range(1, 2 * n, 2):
        producto *= i
    return producto
# Medir tiempo de ejecución
def medir_tiempo_ejecucion(n):
    start_time = time.time()
    resultado = productoNImpares(n)
    end_time = time.time()
    tiempo_transcurrido = end_time - start_time
    print(f"Resultado productoNImpares({n}) = {resultado}")
    print(f"Tiempo de ejecución: {tiempo_transcurrido:.6f} segundos") 
    return tiempo_transcurrido 
# Ejemplo de uso
n = 10
medir_tiempo_ejecucion(n)
