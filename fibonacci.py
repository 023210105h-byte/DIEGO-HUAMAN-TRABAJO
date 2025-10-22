def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n- 1) + fibonacci(n - 2)
def mostrar_fibonacci(n):
    for i in range(n):
        print(fibonacci(i), end=" ")
    print()
# Ejemplo de uso
mostrar_fibonacci(10)