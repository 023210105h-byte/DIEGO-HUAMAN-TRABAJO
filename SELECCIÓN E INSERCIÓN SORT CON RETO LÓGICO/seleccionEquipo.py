def ordenar_equipo(fuerzas):
    n = len(fuerzas)
    for i in range(n-1):
        min = i
        for j in range(i+1, n):
            if fuerzas[j] < fuerzas[min]:
                min = j
        fuerzas[i], fuerzas[min] = fuerzas[min], fuerzas[i]
        print(f"la interaccion es:{i+1} -- {fuerzas}")
    return fuerzas

fuerzas = [40, 30, 90, 20, 10]
print("el orden de los guerrero segun su fuerza es: ", ordenar_equipo(fuerzas))