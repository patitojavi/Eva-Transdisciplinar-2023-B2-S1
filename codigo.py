import tkinter as tk
from tkinter import * 
from math import sin, cos, pi
import math
import pygame 

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

# Cálculo de las componentes de la gravedad
angulo_rad = inclinacion * pi / 180
fuerza_gravedad = masa * gravedad * sin(angulo_rad)
fuerza_friction = friccion * fuerza_gravedad

def ventana_principal():
    ventana = tk.Tk()
    ventana.title('Plano Inclinado Dinamica')
    ventana.geometry("1280x700")
    ventana.resizable(False, False)
    ventana.configure(bg='#06283D')

    fondo1=Frame(ventana, bg= "#47B5FF")
    fondo1.place(x = 0, y = 0, width= 375 , height= 347)
    fondo1.config(relief="sunken") 
    fondo1.config(bd=10)

    fondo2 = Frame(ventana, bg= "#06283D")
    fondo2.place(x = 7, y = 9, width= 360 , height= 330)
    fondo2.config(relief="sunken") 
    fondo2.config(bd=2)

    f1=Frame(ventana, bg= "#47B5FF")
    f1.place(x = 0, y = 350, width= 375 , height= 350)
    f1.config(relief="sunken") 
    f1.config(bd=10)

    f2 = Frame(ventana, bg= "#06283D")
    f2.place(x = 5 , y = 357 , width= 365 , height= 335)
    f2.config(relief="sunken") 
    f2.config(bd=2)

    lblMasa = tk.Label(fondo2, text="Masa (kg):",padx=20)
    lblMasa.pack()
    txtMasa = tk.Entry(fondo2)
    txtMasa.pack()

    lblAngulo = tk.Label(fondo2, text="Ángulo (grados):",padx=20)
    lblAngulo.pack()
    txtAngulo = tk.Entry(fondo2)
    txtAngulo.pack()

    lblCoefFriccion = tk.Label(fondo2, text="Coef. de Fricción:", padx=20)
    lblCoefFriccion.pack()
    txtCoefFriccion = tk.Entry(fondo2)
    txtCoefFriccion.pack()

    btnCalcular = tk.Button(fondo2, text="Calcular", command=calcular_plano_inclinado)
    btnCalcular.pack()
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





ventana_principal()
