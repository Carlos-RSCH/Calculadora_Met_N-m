# Importar Librerías
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
from sympy import symbols, lambdify, diff, sympify
import tkinter as tk
from tkinter import ttk, messagebox

def desarrollo():
    metodo_seleccionado = metodo.get()

    text.delete(1.0, tk.END)
    x = symbols('x')

    try:
        fn = sympify(funcion.get())  # Validar si la función ingresada es correcta
        f = lambdify(x, fn)
        f_prime = lambdify(x, diff(fn, x))  # Derivada para Newton-Raphson
    except:
        messagebox.showerror("Error", "La función ingresada no es válida. Por favor, verifica la expresión.")
        return

    try:
        a = float(valorA.get())  # Validar el valor de 'a'
        b = float(valorB.get())  # Validar el valor de 'b'
        crit = float(umbral.get())  # Validar el umbral
        imax = int(maxIter.get())  # Validar las iteraciones máximas
    except:
        messagebox.showerror("Error", "Uno o más valores ingresados no son válidos. Por favor, verifica las entradas.")
        return

    if metodo_seleccionado in ("Bisección", "Falsa Posición"):
        if f(a) * f(b) >= 0:  # Condición para que la función cambie de signo en [a, b]
            messagebox.showerror("Error", "Los valores de 'a' y 'b' no cumplen con la condición f(a) * f(b) < 0. Por favor, verifica las entradas.")
            return

    i = 0
    ea = 100
    x_anterior = None

    # Encabezado de la tabla
    text.insert(tk.END, f"{'Método de ' + metodo_seleccionado:^80}\n")
    if metodo_seleccionado == "Newton-Raphson":
        text.insert(tk.END, f"{'i':^5} {'a':^12} {'b':^12} {'xr':^12} {'f(xr)':^12} {'f\'(xr)':^12}\n")
    else:
        text.insert(tk.END, f"{'i':^5} {'a':^12} {'b':^12} {'xr':^12} {'f(xr)':^12}\n")

    if metodo_seleccionado == "Falsa Posición":
        a_falsa = float(valorA.get())
        b_falsa = float(valorB.get())

        fa = f(a_falsa)
        fb = f(b_falsa)

        while i < imax:  # Ejecutar exactamente maxIter veces
            # Calcular xr
            xr = b_falsa - fb * (a_falsa - b_falsa) / (fa - fb)
            fxr = f(xr)

            # Mostrar resultados en cada iteración
            text.insert(tk.END, f"{i:^5} {a_falsa:^12.6f} {b_falsa:^12.6f} {xr:^12.6f} {fxr:^12.6f}\n")

            # Actualizar los límites a_falsa y b_falsa
            if fa * fxr < 0:
                b_falsa = xr
                fb = f(b_falsa)
            else:
                a_falsa = xr
                fa = f(a_falsa)

            i += 1

        resultado_final = xr  # Resultado final

    elif metodo_seleccionado == "Newton-Raphson":
        xr = a  # Valor inicial
        while i < imax:
            fxr = f(xr)
            fxr_prime = f_prime(xr)

            if fxr_prime == 0:
                messagebox.showerror("Error", "La derivada en el punto es cero, no se puede aplicar Newton-Raphson.")
                return

            # Mostrar resultados en cada iteración
            text.insert(tk.END, f"{i:^5} {xr:^12.6f} {'-':^12} {xr:^12.6f} {fxr:^12.6f} {fxr_prime:^12.6f}\n")

            # Calcular nuevo xr
            xr = xr - fxr / fxr_prime
            i += 1

        resultado_final = xr  # Resultado final

    elif metodo_seleccionado == "Bisección":
        while i < imax:
            xr = (a + b) / 2
            fxr = f(xr)

            # Mostrar resultados en cada iteración
            text.insert(tk.END, f"{i:^5} {a:^12.6f} {b:^12.6f} {xr:^12.6f} {fxr:^12.6f}\n")

            # Actualizar los límites a y b
            if f(a) * fxr < 0:
                b = xr
            else:
                a = xr

            i += 1

        resultado_final = xr  # Resultado final

    # Mostrar el resultado final en la tabla
    text.insert(tk.END, f"\nEl valor de x es {resultado_final:.9f}\n")

    # Graficar la función
    xpts = np.linspace(-10, 10)
    ax.clear()
    ax.plot(xpts, f(xpts))
    ax.axhline(color="black")
    ax.axvline(color="black")
    ax.scatter(resultado_final, 0, c="red")
    ax.annotate(f"{resultado_final:.9f}", xy=(resultado_final, 0.5))
    ax.set_title("Gráfica de la Función")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.grid(True, which='both')
    ax.set_ylim([-15, 15])
    canvas.draw()

# Crear ventana
ventana = tk.Tk()
ventana.title("Calculadora de Métodos de Bisección, Falsa Posición y Newton-Raphson")

# Etiquetas y entradas
ttk.Label(ventana, text="Agregue una Función f(x): ").grid(column=0, row=2)
ttk.Label(ventana, text="Método: ").grid(column=0, row=4)
ttk.Label(ventana, text="Ingresa un Valor a").grid(column=3, row=2)
ttk.Label(ventana, text="Ingresa un Valor b: ").grid(column=3, row=4)
ttk.Label(ventana, text="Umbral: ").grid(column=5, row=2)
ttk.Label(ventana, text="Máx Inter: ").grid(column=5, row=4)

funcion = tk.StringVar()
ttk.Entry(ventana, width=20, textvariable=funcion).grid(column=1, row=2)

valorA = tk.StringVar()
ttk.Entry(ventana, width=20, textvariable=valorA).grid(column=4, row=2)

valorB = tk.StringVar()
ttk.Entry(ventana, width=20, textvariable=valorB).grid(column=4, row=4)

umbral = tk.StringVar()
ttk.Entry(ventana, width=20, textvariable=umbral).grid(column=6, row=2)

maxIter = tk.StringVar()
ttk.Entry(ventana, width=20, textvariable=maxIter).grid(column=6, row=4)

# Botón
ttk.Button(ventana, text="Generar", command=desarrollo).grid(column=7, row=2)

# Cuadro de texto
text = tk.Text(ventana, width=80, height=20)
text.grid(row=5, column=0)

# Gráfica
figure = plt.Figure(figsize=(10, 8), dpi=50)
ax = figure.add_subplot(111)
canvas = FigureCanvasTkAgg(figure, ventana)
canvas.get_tk_widget().grid(row=5, column=2, columnspan=5, rowspan=5)

# ComboBox Método
metodo = tk.StringVar()
seleccionar_metodo = ttk.Combobox(ventana, width=12, textvariable=metodo)
seleccionar_metodo['values'] = ("Bisección", "Falsa Posición", "Newton-Raphson")
seleccionar_metodo.grid(column=1, row=4)
seleccionar_metodo.current(0)

ventana.mainloop()