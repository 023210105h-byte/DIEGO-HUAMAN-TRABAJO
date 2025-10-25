def suma_lista(lista):
    if not lista:
        return 0
    return lista[0] + suma_lista(lista[1:])
lista = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
print(suma_lista(lista))