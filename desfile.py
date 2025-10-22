def burbujaNombres(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n-i-1):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
    return lista

nombres = ["Carlos", "Ana", "Pedro", "Lucía", "Diego"]
print("Lista original:", nombres)
resultado = burbujaNombres(nombres)
print("Lista ordenada alfabéticamente:", resultado)

