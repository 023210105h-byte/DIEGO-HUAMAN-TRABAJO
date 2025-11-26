from tkinter import *

ventana = Tk()
ventana.geometry("640x260")
ventana.title("Conversión Fahrenheit a Celsius")
ventana.resizable(False, False)

contenedor = Frame(ventana)
contenedor.pack(fill="both", expand=True)
contenedor.config(bg="#f4f6f6")

lbl_titulo = Label(contenedor, text="CONVERSIÓN DE FAHRENHEIT A CELSIUS",
                   font=("Times New Roman", 16), fg="#216B2C", bg="#f4f6f6")
lbl_titulo.grid(row=0, column=2, pady=15)

Label(contenedor, text="Ingrese grados Fahrenheit:", bg="#f4f6f6").grid(row=1, column=1, padx=15, pady=10, sticky="e")
txt_fahrenheit = Entry(contenedor)
txt_fahrenheit.grid(row=1, column=2, padx=15, pady=10)

Label(contenedor, text="Resultado:", bg="#f4f6f6").grid(row=3, column=1, padx=15, pady=10, sticky="e")
txt_resultado = Entry(contenedor)
txt_resultado.grid(row=3, column=2, padx=15, pady=10)

def convertir():
    try:

        if txt_fahrenheit.get() == "":
            txt_resultado.delete(0, "end")
            txt_resultado.insert("end", "Error: Ingrese un valor")
            return

        f = float(txt_fahrenheit.get())

        c = (5/9) * (f - 32)

        txt_resultado.delete(0, "end")
        txt_resultado.insert("end", f"{f}°F equivale a {round(c, 2)}°C")

    except:
        txt_resultado.delete(0, "end")
        txt_resultado.insert("end", "Error: Solo números válidos")

btn_convertir = Button(contenedor, text="Convertir", padx=5, pady=5,
                       bg="purple", fg="#ffffff", command=convertir)
btn_convertir.grid(row=2, column=2, pady=10)

ventana.mainloop()