def burbujaContador(lista):
    n = len(lista)
    comparaciones = 0
    intercambios = 0
    for i in range(n):
        for j in range(0, n-i-1):
            comparaciones += 1
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
                intercambios += 1

    print("Total de comparaciones:", comparaciones)
    print("Total de intercambios:", intercambios)
    return lista

numeros = [5, 3, 8, 4, 2]
print("Lista original:", numeros)
resultado = burbujaContador(numeros)
print("Lista ordenada:", resultado)
