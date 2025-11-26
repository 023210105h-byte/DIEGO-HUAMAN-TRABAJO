from tkinter import *

ventana = Tk()
ventana.geometry("700x380")
ventana.title("Cálculo de Salario con Horas Extras")
ventana.resizable(False, False)

contenedor = Frame(ventana)
contenedor.pack(fill="both", expand=True)
contenedor.config(bg="#f4f6f6")

lbl_titulo = Label(contenedor, text="CÁLCULO DE SALARIO CON HORAS EXTRAS",
                   font=("Times New Roman", 16), fg="#216B2C", bg="#f4f6f6")
lbl_titulo.grid(row=0, column=2, pady=15)

Label(contenedor, text="Ingrese horas trabajadas:", bg="#f4f6f6").grid(row=1, column=1, padx=15, pady=10, sticky="e")
txt_horas = Entry(contenedor)
txt_horas.grid(row=1, column=2, padx=15, pady=10)

Label(contenedor, text="Ingrese tarifa por hora (S/):", bg="#f4f6f6").grid(row=2, column=1, padx=15, pady=10, sticky="e")
txt_tarifa = Entry(contenedor)
txt_tarifa.grid(row=2, column=2, padx=15, pady=10)

Label(contenedor, text="Resultado:", bg="#f4f6f6").grid(row=4, column=1, padx=15, pady=10, sticky="e")
txt_resultado = Entry(contenedor, width=40)
txt_resultado.grid(row=4, column=2, padx=15, pady=10)

def calcular_salario():
    try:
        
        if txt_horas.get() == "" or txt_tarifa.get() == "":
            txt_resultado.delete(0, "end")
            txt_resultado.insert("end", "Error: Complete todos los campos")
            return

        horas = float(txt_horas.get())
        tarifa = float(txt_tarifa.get())

        if horas < 0:
            txt_resultado.delete(0, "end")
            txt_resultado.insert("end", "Error: Horas no pueden ser negativas")
            return

        if tarifa <= 0:
            txt_resultado.delete(0, "end")
            txt_resultado.insert("end", "Error: La tarifa debe ser mayor que 0")
            return

        if horas <= 40:
            salario = horas * tarifa
            extras = 0
            tarifa_extra = tarifa * 1.5
        else:
            horas_normales = 40
            extras = horas - 40
            tarifa_extra = tarifa * 1.5
            salario = (horas_normales * tarifa) + (extras * tarifa_extra)

        mensaje = (f"Horas trabajadas: {horas} | "
                   f"Tarifa normal: S/ {round(tarifa, 2)} | "
                   f"Horas extras: {extras} a S/ {round(tarifa_extra, 2)} | "
                   f"Salario total: S/ {round(salario, 2)}")

        txt_resultado.delete(0, "end")
        txt_resultado.insert("end", mensaje)

    except:
        txt_resultado.delete(0, "end")
        txt_resultado.insert("end", "Error: Solo números válidos")

btn_calcular = Button(contenedor, text="Calcular salario", padx=5, pady=5,
                      bg="purple", fg="#ffffff", command=calcular_salario)
btn_calcular.grid(row=3, column=2, pady=10)

ventana.mainloop()