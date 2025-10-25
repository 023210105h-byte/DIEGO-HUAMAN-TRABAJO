import random
import time

def insertionSort(lista):
    comparaciones = 0
    n = len(lista)
    for i in range(1, n):
        j = i
        while j > 0:
            comparaciones += 1
            if lista[j] < lista[j-1]:
                lista[j], lista[j-1] = lista[j-1], lista[j]
                j -= 1
            else:
                break
    return lista, comparaciones


def selectionSort(lista):
    comparaciones = 0
    n = len(lista)
    for i in range(n - 1):
        minimo = i
        for j in range(i + 1, n):
            comparaciones += 1
            if lista[j] < lista[minimo]:
                minimo = j
        lista[i], lista[minimo] = lista[minimo], lista[i]
    return lista, comparaciones


def medir_algoritmo(funcion, lista):
    copia = lista.copy()
    inicio = time.time()
    resultado, comparaciones = funcion(copia)
    fin = time.time()
    return comparaciones, fin - inicio


def menu():
    while True:
        print("\n--- MENÚ DE OPERACIÓN ---")
        print("1. Generar lista de 100 números aleatorios")
        print("2. Ordenar con Insertion Sort y Selection Sort")
        print("3. Salir")
        opcion = input("Elige una opción: ")

        if opcion == "1":
            global lista
            lista = [random.randint(1, 1000) for _ in range(100)]
            print("Lista generada:", lista)
        elif opcion == "2":
            if 'lista' not in globals():
                print("Primero debes generar la lista (opción 1).")
                continue
            print("\nOrdenando con Insertion Sort...")
            comp_ins, tiempo_ins = medir_algoritmo(insertionSort, lista)
            print(f"Comparaciones: {comp_ins}")
            print(f"Tiempo: {tiempo_ins:.6f} segundos")

            print("\nOrdenando con Selection Sort...")
            comp_sel, tiempo_sel = medir_algoritmo(selectionSort, lista)
            print(f"Comparaciones: {comp_sel}")
            print(f"Tiempo: {tiempo_sel:.6f} segundos")

            print("\n--- Análisis ---")
            if tiempo_ins < tiempo_sel:
                print("Insertion Sort fue más eficiente en tiempo.")
            else:
                print("Selection Sort fue más eficiente en tiempo.")

            if comp_ins < comp_sel:
                print("Insertion Sort hizo menos comparaciones.")
            else:
                print("Selection Sort hizo menos comparaciones.")
        elif opcion == "3":
            print("Saliendo...")
            break
        else:
            print("Opción inválida. Intenta de nuevo.")
menu()