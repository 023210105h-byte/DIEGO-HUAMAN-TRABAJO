import random
def desafioBotin(lista):
    n=len(lista)
    for i in range(1, n):
        while i > 0 and lista[i] < lista[i - 1]:
            lista[i], lista[i - 1] = lista[i - 1], lista[i]
            i = i - 1
    return lista
lista = [10, 5, 25, 1, 8]
print("El orden de las monedas de oro para que entren en el compartimento secreto de menor a mayor es:", desafioBotin(lista))