import tkinter as tk
from tkinter import ttk, messagebox

ventana = tk.Tk()
ventana.title("Calculadora Básica")
ventana.geometry("400x300")

frame = ttk.Frame(ventana, padding=20)
frame.grid(row=0, column=0)

def validar_entradas():
    num1 = txt_num1.get().strip()
    num2 = txt_num2.get().strip()

    if num1 == "" or num2 == "":
        messagebox.showerror("Error", "Error: ambos campos deben estar llenos.")
        return None

    try:
        return float(num1), float(num2)
    except ValueError:
        messagebox.showerror("Error", "Error: solo se permiten números.")
        return None

def mostrar_resultado(texto):
    lbl_resultado.config(text=texto)

def sumar():
    datos = validar_entradas()
    if datos:
        a, b = datos
        mostrar_resultado(f"Resultado de la suma: {a + b}")

def restar():
    datos = validar_entradas()
    if datos:
        a, b = datos
        mostrar_resultado(f"Resultado de la resta: {a - b}")

def multiplicar():
    datos = validar_entradas()
    if datos:
        a, b = datos
        mostrar_resultado(f"Resultado de la multiplicación: {a * b}")

def dividir():
    datos = validar_entradas()
    if datos:
        a, b = datos
        if b == 0:
            messagebox.showerror("Error", "Error: no se puede dividir entre cero.")
            return
        mostrar_resultado(f"Resultado de la división: {a / b:.2f}")

def limpiar():
    txt_num1.delete(0, tk.END)
    txt_num2.delete(0, tk.END)
    lbl_resultado.config(text="Resultado:")

def salir():
    ventana.destroy()

ttk.Label(frame, text="Calculadora Básica", font=("Arial", 16, "bold")).grid(row=0, column=0, columnspan=2, pady=10)

ttk.Label(frame, text="Número 1:").grid(row=1, column=0, sticky="e", pady=5)
txt_num1 = ttk.Entry(frame)
txt_num1.grid(row=1, column=1, pady=5)

ttk.Label(frame, text="Número 2:").grid(row=2, column=0, sticky="e", pady=5)
txt_num2 = ttk.Entry(frame)
txt_num2.grid(row=2, column=1, pady=5)

ttk.Button(frame, text="Sumar", width=15, command=sumar).grid(row=3, column=0, pady=5)

ttk.Button(frame, text="Restar", width=15, command=restar).grid(row=3, column=1, pady=5)

ttk.Button(frame, text="Multiplicar", width=15, command=multiplicar).grid(row=4, column=0, pady=5)

ttk.Button(frame, text="Dividir", width=15, command=dividir).grid(row=4, column=1, pady=5)

ttk.Button(frame, text="Limpiar", width=15, command=limpiar).grid(row=5, column=0, pady=10)

ttk.Button(frame, text="Salir", width=15, command=salir).grid(row=5, column=1, pady=10)

lbl_resultado = ttk.Label(frame, text="Resultado:", font=("Arial", 11, "bold"))
lbl_resultado.grid(row=6, column=0, columnspan=2, pady=10)

ventana.mainloop()
