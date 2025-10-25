def burbujaNumeros(lista):
    n = len(lista)
    paso = 0
    for i in range(n):
        for j in range(0, n-i-1):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
                paso += 1
                print(f"Paso {paso}: {lista}")
    return lista

numeros = [5, 3, 8, 4, 2]
print("Lista original:", numeros)
resultado = burbujaNumeros(numeros)
print("Lista ordenada:", resultado)
