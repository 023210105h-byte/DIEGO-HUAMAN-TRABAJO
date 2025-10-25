import random
def busqueda_secuencial(lista, numero):
    comparaciones = 0
    for i, val in enumerate(lista):
        comparaciones += 1
        if val == numero:
            return i, comparaciones
    return -1, comparaciones
def esta_ordenada(lista):
    return all(lista[i] <= lista[i+1] for i in range(len(lista)-1))
def ordenar_lista_en_lugar(lista):
    lista.sort()
def busqueda_binaria(lista, numero):
    # caso lista vacía
    if len(lista) == 0:
        return -1, 0
    if not esta_ordenada(lista):
        lista.sort()
        print(" La lista no estaba ordenada. Se ordenó automáticamente para la búsqueda binaria.")
    izquierda, derecha = 0, len(lista) - 1
    iteraciones = 0
    while izquierda <= derecha:
        iteraciones += 1
        medio = (izquierda + derecha) // 2
        if lista[medio] == numero:
            return medio, iteraciones
        elif lista[medio] < numero:
            izquierda = medio + 1
        else:
            derecha = medio - 1
    return -1, iteraciones
def menu():
    lista = []
    while True:
        print("\n=== MENÚ PRINCIPAL ===")
        print("1) Generar lista aleatoria")
        print("2) Ordenar lista")
        print("3) Buscar elemento (Secuencial)")
        print("4) Buscar elemento (Binaria)")
        print("5) Comparar eficiencia (K búsquedas)")
        print("6) Mostrar lista (breve)")
        print("7) Salir")
        opcion = input("Elige opción (1-7): ").strip()
        if opcion == "1":
            try:
                n = int(input("Tamaño de la lista (ej: 100): "))
                if n <= 0:
                    print("Ingresa un tamaño positivo.")
                    continue
            except ValueError:
                print("Entrada no válida. Debes ingresar un número entero.")
                continue
            lista = [random.randint(1, 1000) for _ in range(n)]
            print(f" Lista generada con {len(lista)} elementos.")
        elif opcion == "2":
            if not lista:
                print(" Primero genera la lista (opción 1).")
            else:
                ordenar_lista_en_lugar(lista)
                print(" Lista ordenada.")
        elif opcion == "3":
            if not lista:
                print(" Primero genera la lista (opción 1).")
                continue
            try:
                numero = int(input("Número a buscar: "))
            except ValueError:
                print("Entrada no válida.")
                continue
            pos, comp = busqueda_secuencial(lista, numero)
            if pos == -1:
                print(f"No se encontró {numero}. Comparaciones realizadas: {comp}")
            else:
                print(f"{numero} encontrado en índice {pos}. Comparaciones: {comp}")
        elif opcion == "4":
            if not lista:
                print(" Primero genera la lista (opción 1).")
                continue
            try:
                numero = int(input("Número a buscar: "))
            except ValueError:
                print("Entrada no válida.")
                continue
            pos, it = busqueda_binaria(lista, numero)
            if pos == -1:
                print(f"No se encontró {numero}. Iteraciones: {it}")
            else:
                print(f"{numero} encontrado en índice {pos} (lista ordenada). Iteraciones: {it}")
        elif opcion == "5":
            if not lista:
                print(" Primero genera la lista (opción 1).")
                continue
            try:
                k = int(input("Número de búsquedas aleatorias (K): "))
                if k <= 0:
                    print("Ingresa un K positivo.")
                    continue
            except ValueError:
                print("Entrada no válida.")
                continue
            auto_sorted = False
            if not esta_ordenada(lista):
                lista.sort()
                auto_sorted = True
                print(" La lista no estaba ordenada. Se ordenó automáticamente para el experimento.")
            total_sec = 0
            total_bin = 0
            for _ in range(k):
                numero = random.choice(lista)
                _, comp = busqueda_secuencial(lista, numero)  
                _, it = busqueda_binaria(lista, numero)      
                total_sec += comp
                total_bin += it
            prom_sec = total_sec / k
            prom_bin = total_bin / k
            ratio = (prom_sec / prom_bin) if prom_bin != 0 else float('inf')
            print(f"\n Promedio Secuencial (K={k}): {prom_sec:.2f} comparaciones")
            print(f" Promedio Binaria   (K={k}): {prom_bin:.2f} iteraciones")
            print(f" Ratio Sec/Bin: {ratio:.2f}")
            if auto_sorted:
                print("Nota: para que la comparación sea coherente la lista se usó ordenada (binaria exige orden).")
        elif opcion == "6":
            if not lista:
                print("Lista vacía.")
            else:
                muestra = lista if len(lista) <= 50 else lista[:50]
                print(f"Mostrando primeros {len(muestra)} elementos: {muestra}")
                if len(lista) > 50:
                    print(f"... (y {len(lista)-50} elementos más)")
        elif opcion == "7":
            print("Saliendo.")
            break
        else:
            print("Opción no válida. Elige un número entre 1 y 7.")
if __name__ == "__main__":
    menu()
