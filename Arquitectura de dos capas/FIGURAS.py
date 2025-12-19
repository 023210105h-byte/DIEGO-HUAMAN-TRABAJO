import tkinter as tk
from tkinter import ttk, messagebox
import math

root = tk.Tk()
root.title("Áreas de Figuras Geométricas")
root.geometry("500x300")
root.resizable(False, False)

main_frame = ttk.Frame(root, padding=20)
main_frame.grid(row=0, column=0)

ttk.Label(main_frame, text="Cálculo de Áreas", font=("Arial", 16, "bold")).grid(row=0, column=0, columnspan=2, pady=10)

def area_circulo(radio):
    return math.pi * radio ** 2

def area_rectangulo(base, altura):
    return base * altura

def area_triangulo(base, altura):
    return (base * altura) / 2

def abrir_circulo():
    modal = tk.Toplevel(root)
    modal.title("Área del Círculo")
    modal.geometry("300x200")
    modal.resizable(False, False)
    modal.grab_set()

    frame = ttk.Frame(modal, padding=15)
    frame.grid(row=0, column=0)

    ttk.Label(frame, text="Radio:").grid(row=0, column=0, pady=5, sticky="e")
    txt_radio = ttk.Entry(frame)
    txt_radio.grid(row=0, column=1, pady=5)

    def calcular():
        try:
            r = float(txt_radio.get())
            if r <= 0:
                raise ValueError
            resultado = area_circulo(r)
            messagebox.showinfo("Resultado", f"Área del círculo: {resultado:.2f}")
        except ValueError:
            messagebox.showerror("Error", "Ingrese un radio válido.")

    ttk.Button(frame, text="Calcular", command=calcular).grid(row=1, column=0, pady=10)
    ttk.Button(frame, text="Cerrar", command=modal.destroy).grid(row=1, column=1, pady=10)

def abrir_rectangulo():
    modal = tk.Toplevel(root)
    modal.title("Área del Rectángulo")
    modal.geometry("300x220")
    modal.resizable(False, False)
    modal.grab_set()

    frame = ttk.Frame(modal, padding=15)
    frame.grid(row=0, column=0)

    ttk.Label(frame, text="Base:").grid(row=0, column=0, pady=5, sticky="e")
    txt_base = ttk.Entry(frame)
    txt_base.grid(row=0, column=1, pady=5)

    ttk.Label(frame, text="Altura:").grid(row=1, column=0, pady=5, sticky="e")
    txt_altura = ttk.Entry(frame)
    txt_altura.grid(row=1, column=1, pady=5)

    def calcular():
        try:
            base = float(txt_base.get())
            altura = float(txt_altura.get())
            if base <= 0 or altura <= 0:
                raise ValueError
            resultado = area_rectangulo(base, altura)
            messagebox.showinfo("Resultado", f"Área del rectángulo: {resultado:.2f}")
        except ValueError:
            messagebox.showerror("Error", "Ingrese valores válidos.")

    ttk.Button(frame, text="Calcular", command=calcular).grid(row=2, column=0, pady=10)
    ttk.Button(frame, text="Cerrar", command=modal.destroy).grid(row=2, column=1, pady=10)

def abrir_triangulo():
    modal = tk.Toplevel(root)
    modal.title("Área del Triángulo")
    modal.geometry("300x240")
    modal.resizable(False, False)
    modal.grab_set()

    frame = ttk.Frame(modal, padding=15)
    frame.grid(row=0, column=0)

    ttk.Label(frame, text="Base:").grid(row=0, column=0, pady=5, sticky="e")
    txt_base = ttk.Entry(frame)
    txt_base.grid(row=0, column=1, pady=5)

    ttk.Label(frame, text="Altura:").grid(row=1, column=0, pady=5, sticky="e")
    txt_altura = ttk.Entry(frame)
    txt_altura.grid(row=1, column=1, pady=5)

    def calcular():
        try:
            base = float(txt_base.get())
            altura = float(txt_altura.get())
            if base <= 0 or altura <= 0:
                raise ValueError
            resultado = area_triangulo(base, altura)
            messagebox.showinfo("Resultado", f"Área del triángulo: {resultado:.2f}")
        except ValueError:
            messagebox.showerror("Error", "Ingrese valores válidos.")

    ttk.Button(frame, text="Calcular", command=calcular).grid(row=2, column=0, pady=10)
    ttk.Button(frame, text="Cerrar", command=modal.destroy).grid(row=2, column=1, pady=10)

ttk.Button(main_frame, text="Área del Círculo", width=20, command=abrir_circulo).grid(row=1, column=0, pady=5)

ttk.Button(main_frame, text="Área del Rectángulo", width=20, command=abrir_rectangulo).grid(row=2, column=0, pady=5)

ttk.Button(main_frame, text="Área del Triángulo", width=20, command=abrir_triangulo).grid(row=3, column=0, pady=5)

root.mainloop()