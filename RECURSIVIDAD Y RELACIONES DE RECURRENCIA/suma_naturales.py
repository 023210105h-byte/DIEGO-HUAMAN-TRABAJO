def suma_naturales(n):
    if n == 0:
        return 0
    return n + suma_naturales(n - 1)
print(suma_naturales(5))