import random
def busqueda_secuencial(lista, dni):
    comparaciones = 0
    for i in range(len(lista)):
        comparaciones += 1
        if lista[i] == dni:
            return i, comparaciones 
    return -1, comparaciones
lista = [random.randint(10000000, 99999999) for _ in range(60)]
print("Lista generada:", lista)
dni1 = -1             
dni2 = lista[0]
dni3 = lista[-1]
dni4 = lista[len(lista)//2]
print("--- Resultados Búsqueda Secuencial ---")
for dni in [dni1, dni2, dni3, dni4]:
    pos, comp = busqueda_secuencial(lista, dni)
    print(f"Buscando {dni} → Posición: {pos}, Comparaciones: {comp}")

print("Conclusión:")
print("La búsqueda secuencial conviene en listas pequeñas o no ordenadas,")
print("pues no requiere ordenar antes y es fácil de implementar.")