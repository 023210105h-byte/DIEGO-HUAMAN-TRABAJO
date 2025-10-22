import time
def sumaSubarreglos(arr):
    suma = 0
    for subarr in arr:
        for num in subarr:
            suma += num
    return suma

def medir_tiempo_ejecucion(arr):
    start_time = time.time()
    resultado = sumaSubarreglos(arr)
    end_time = time.time()
    tiempo_transcurrido = end_time - start_time
    print(f"Resultado sumaSubarreglos({arr}) = {resultado}")
    print(f"Tiempo de ejecución: {tiempo_transcurrido:.6f} segundos")
    return tiempo_transcurrido
arr = [[1, 2, 3], [4, 5], [6]]
medir_tiempo_ejecucion(arr)