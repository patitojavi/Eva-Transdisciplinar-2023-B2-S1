import tkinter as tk
from tkinter import * 
from math import sin, cos, pi
import math


# Parámetros físicos
masa = 1  # kg
gravedad = 9.8  # m/s^2
friccion = 0.2  # coeficiente de fricción
inclinacion = 30  # ángulo de inclinación en grados

# Constantes para la animación
width = 600
height = 400
plano_color = 'gray'
caja_color = 'red'
caja_width = 40
caja_height = 20

import tkinter as tk
from PIL import ImageTk, Image 

ventana = tk.Tk()
ventana.title("Plano Inclinado")
ventana.geometry("1340x745")
ventana.resizable(False, False)

def obtener_datos():
    print("Datos ingresados")
    print("="* 50)
    print("Grado de Inclinacion:", entrada1.get())
    print("Coeficiente de Fricción:", entrada2.get())
    print("Masa en Kilogramos:", entrada3.get())
    print("="* 50)


marco1 = tk.Frame(ventana, bg="white", width=400, height=360)
marco1.grid(row=0, column=0, padx=1, pady=1)
etiqueta1 = tk.Label(marco1, text="Grado de Inclinación:")
etiqueta1.grid(row=0, column=0, padx=10, pady=10)
entrada1 = tk.Entry(marco1)
entrada1.grid(row=0, column=2, padx=10, pady=10)

etiqueta2 = tk.Label(marco1, text="Coeficiente de Fricción:")
etiqueta2.grid(row=1, column=0, padx=10, pady=10)
entrada2 = tk.Entry(marco1)
entrada2.grid(row=1, column=2, padx=10, pady=10)

etiqueta3 = tk.Label(marco1, text="Masa en Kilogramos:")
etiqueta3.grid(row=2, column=0, padx=10, pady=10)
entrada3 = tk.Entry(marco1)
entrada3.grid(row=2, column=2,padx=10, pady=10)

boton_obtener_datos = tk.Button(marco1, text="Calcular:", command=obtener_datos)
boton_obtener_datos.grid(row=3, column=1, padx=10, pady=10)




marco2 = tk.Frame(ventana, bg="black", width=420, height=520)
marco2.grid(row=1, column=0, padx=10, pady=1)
image = Image.open("dcl_pi.png")
photo = ImageTk.PhotoImage(image)
imagen = tk.Label(marco2, image=photo)
imagen.grid(row=1, column= 0)



marco3 = tk.Frame(ventana, bg="black", width=880, height=730)
marco3.grid(row=0, column=1, rowspan=2, padx=10, pady=5)


ventana.mainloop()

def calcular_plano_inclinado(txtMasa, txtAngulo, txtCoefFriccion,fon):
    masa = float(txtMasa.get())
    angulo = float(txtAngulo.get())
    coef_friccion = float(txtCoefFriccion.get())

    # Cálculos del plano inclinado
    fuerza_gravedad = masa * 9.8  # Fuerza de gravedad en Newtons
    fuerza_friction = coef_friccion * fuerza_gravedad * math.cos(math.radians(angulo))  # Fuerza de fricción en Newtons

    # Mostrar resultados en la consola
    print("Fuerza de gravedad:", fuerza_gravedad, "N")
    print("Fuerza de fricción:", fuerza_friction, "N")

    return