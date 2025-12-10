import tkinter as tk
from tkinter import ttk, messagebox
import math

root = tk.Tk()
root.title("Áreas de Figuras Geométricas")
root.geometry("1000x400")

img_circulo = tk.PhotoImage(file="250px-Circle_-_black_simple.svg.png").subsample(3,3)
img_cuadrado = tk.PhotoImage(file="png-transparent-square-border-illustration-square-black-and-white-fuchsia-frame-miscellaneous-angle-white.png").subsample(3,3)
img_triangulo = tk.PhotoImage(file="png-transparent-triangle-drawing-coloring-book-area-ausmalbild-unicornio-angle-rectangle-symmetry.png").subsample(3,3)
img_pentagono = tk.PhotoImage(file="pentagono.png").subsample(3,3)

display = ttk.Frame(root)
display.pack(pady=20)

def area_circulo(radio):
    return math.pi * (radio ** 2)

def area_cuadrado(lado):
    return lado ** 2

def area_triangulo(base, altura):
    return (base * altura) / 2

def area_pentagono(lado, apotema):
    perimetro = 5 * lado
    return (perimetro * apotema) / 2

def abrir_circulo():
    modal = tk.Toplevel(root)
    modal.title("Área del Círculo")
    modal.geometry("300x200")
    modal.grab_set()

    ttk.Label(modal, text="Radio:").pack(pady=5)
    txt_radio = ttk.Entry(modal)
    txt_radio.pack(pady=5)

    def calcular():
        try:
            r = float(txt_radio.get())
            if r <= 0:
                raise ValueError
            resultado = area_circulo(r)
            messagebox.showinfo("Resultado", f"Área del círculo: {resultado:.2f}")
        except:
            messagebox.showerror("Error", "Ingrese un valor válido para el radio.")

    ttk.Button(modal, text="Calcular", command=calcular).pack(pady=5)
    ttk.Button(modal, text="Cerrar", command=modal.destroy).pack(pady=5)


def abrir_cuadrado():
    modal = tk.Toplevel(root)
    modal.title("Área del Cuadrado")
    modal.geometry("300x200")
    modal.grab_set()

    ttk.Label(modal, text="Lado:").pack(pady=5)
    txt_lado = ttk.Entry(modal)
    txt_lado.pack(pady=5)

    def calcular():
        try:
            lado = float(txt_lado.get())
            if lado <= 0:
                raise ValueError
            resultado = area_cuadrado(lado)
            messagebox.showinfo("Resultado", f"Área del cuadrado: {resultado:.2f}")
        except:
            messagebox.showerror("Error", "Ingrese un valor válido para el lado.")

    ttk.Button(modal, text="Calcular", command=calcular).pack(pady=5)
    ttk.Button(modal, text="Cerrar", command=modal.destroy).pack(pady=5)


def abrir_triangulo():
    modal = tk.Toplevel(root)
    modal.title("Área del Triángulo")
    modal.geometry("300x250")
    modal.grab_set()

    ttk.Label(modal, text="Base:").pack(pady=5)
    txt_base = ttk.Entry(modal)
    txt_base.pack(pady=5)

    ttk.Label(modal, text="Altura:").pack(pady=5)
    txt_altura = ttk.Entry(modal)
    txt_altura.pack(pady=5)

    def calcular():
        try:
            base = float(txt_base.get())
            altura = float(txt_altura.get())
            if base <= 0 or altura <= 0:
                raise ValueError
            resultado = area_triangulo(base, altura)
            messagebox.showinfo("Resultado", f"Área del triángulo: {resultado:.2f}")
        except:
            messagebox.showerror("Error", "Ingrese valores válidos para base y altura.")

    ttk.Button(modal, text="Calcular", command=calcular).pack(pady=5)
    ttk.Button(modal, text="Cerrar", command=modal.destroy).pack(pady=5)


def abrir_pentagono():
    modal = tk.Toplevel(root)
    modal.title("Área del Pentágono")
    modal.geometry("300x250")
    modal.grab_set()

    ttk.Label(modal, text="Lado:").pack(pady=5)
    txt_lado = ttk.Entry(modal)
    txt_lado.pack(pady=5)

    ttk.Label(modal, text="Apotema:").pack(pady=5)
    txt_apotema = ttk.Entry(modal)
    txt_apotema.pack(pady=5)

    def calcular():
        try:
            lado = float(txt_lado.get())
            apotema = float(txt_apotema.get())
            if lado <= 0 or apotema <= 0:
                raise ValueError
            resultado = area_pentagono(lado, apotema)
            messagebox.showinfo("Resultado", f"Área del pentágono: {resultado:.2f}")
        except:
            messagebox.showerror("Error", "Ingrese valores válidos para lado y apotema.")

    ttk.Button(modal, text="Calcular", command=calcular).pack(pady=5)
    ttk.Button(modal, text="Cerrar", command=modal.destroy).pack(pady=5)

figuras = [
    (img_circulo, "Círculo", abrir_circulo),
    (img_cuadrado, "Cuadrado", abrir_cuadrado),
    (img_triangulo, "Triángulo", abrir_triangulo),
    (img_pentagono, "Pentágono", abrir_pentagono)
]

for i, (imagen, nombre, comando) in enumerate(figuras):
    lbl = ttk.Label(display, image=imagen)
    lbl.grid(row=0, column=i, padx=10)

    btn = ttk.Button(display, text=nombre, command=comando)
    btn.grid(row=1, column=i, padx=10, pady=10)

root.mainloop()