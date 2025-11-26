from tkinter import *

ventana = Tk()
ventana.geometry("640x320")
ventana.title("Determinar el Mayor de 3 Números")
ventana.resizable(False, False)

contenedor = Frame(ventana)
contenedor.pack(fill="both", expand=True)
contenedor.config(bg="#f4f6f6")

lbl_titulo = Label(contenedor, text="DETERMINAR EL MAYOR DE 3 NÚMEROS",
                   font=("Times New Roman", 16), fg="#216B2C", bg="#f4f6f6")
lbl_titulo.grid(row=0, column=2, pady=15)

Label(contenedor, text="Ingrese el número 1:", bg="#f4f6f6").grid(row=1, column=1, padx=15, pady=10, sticky="e")
txt_1 = Entry(contenedor)
txt_1.grid(row=1, column=2, padx=15, pady=10)

Label(contenedor, text="Ingrese el número 2:", bg="#f4f6f6").grid(row=2, column=1, padx=15, pady=10, sticky="e")
txt_2 = Entry(contenedor)
txt_2.grid(row=2, column=2, padx=15, pady=10)

Label(contenedor, text="Ingrese el número 3:", bg="#f4f6f6").grid(row=3, column=1, padx=15, pady=10, sticky="e")
txt_3 = Entry(contenedor)
txt_3.grid(row=3, column=2, padx=15, pady=10)

Label(contenedor, text="Resultado:", bg="#f4f6f6").grid(row=5, column=1, padx=15, pady=10, sticky="e")
txt_resultado = Entry(contenedor)
txt_resultado.grid(row=5, column=2, padx=15, pady=10)

def determinar_mayor():
    try:
        if txt_1.get() == "" or txt_2.get() == "" or txt_3.get() == "":
            txt_resultado.delete(0, "end")
            txt_resultado.insert("end", "Error: Ingrese los 3 números")
            return

        n1 = float(txt_1.get())
        n2 = float(txt_2.get())
        n3 = float(txt_3.get())

        maximo = max(n1, n2, n3)

        cantidad_mayores = [n1, n2, n3].count(maximo)

        txt_resultado.delete(0, "end")

        if cantidad_mayores == 1:
            txt_resultado.insert("end", f"El mayor es: {maximo}")
        elif cantidad_mayores == 2:
            txt_resultado.insert("end", f"Hay dos números mayores iguales: {maximo}")
        else:
            txt_resultado.insert("end", f"Los tres números son iguales: {maximo}")

    except:
        txt_resultado.delete(0, "end")
        txt_resultado.insert("end", "Error: Solo números válidos")

btn_calcular = Button(contenedor, text="Determinar mayor", padx=5, pady=5,
                      bg="purple", fg="#ffffff", command=determinar_mayor)
btn_calcular.grid(row=4, column=2, pady=10)

ventana.mainloop()
