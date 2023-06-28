import tkinter as tk
import math
import matplotlib.pyplot as plt
import pygame

def calcular_aceleracion():
    masa = float(entry_masa.get())
    coef_friccion = float(entry_coef_friccion.get())
    grado_inclinacion = float(entry_grado_inclinacion.get())

    angulo_radianes = math.radians(grado_inclinacion)
    aceleracion = (math.sin(angulo_radianes) - coef_friccion * math.cos(angulo_radianes)) * 9.8

    lbl_resultado.configure(text=f"Aceleración: {aceleracion:.2f} m/s^2")

def mostrar_grafico():
    masa = float(entry_masa.get())
    coef_friccion = float(entry_coef_friccion.get())
    tiempo = range(0, 10)
    aceleraciones = []

    for t in tiempo:
        aceleracion = coef_friccion * t
        aceleraciones.append(aceleracion)

    plt.plot(tiempo, aceleraciones)
    plt.xlabel('Tiempo (s)')
    plt.ylabel('Aceleración (m/s^2)')
    plt.title('Gráfico de Aceleración en función del Tiempo')
    plt.grid(True)
    plt.show()

def mostrar_animacion():
    pygame.init()
    width = 800
    height = 600
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Plano inclinado")
    x = 100  
    y = 100  
    radio = 25 
    velocidad = 3 
    angulo = math.radians(30)

    posicion_x = x
    posicion_y = y
    velocidad_x = velocidad * math.cos(angulo)
    velocidad_y = velocidad * math.sin(angulo)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        posicion_x += velocidad_x
        posicion_y += velocidad_y
        if posicion_y >= height - radio * math.cos(angulo):
            posicion_x = x
            posicion_y = y
        screen.fill(WHITE)
        pygame.draw.circle(screen, RED, (int(posicion_x), int(posicion_y)), radio)
        pygame.draw.line(screen, BLACK, (1,68), (799,534), 2)
        pygame.display.flip()
        pygame.time.Clock().tick(60)
    pygame.quit()

ventana = tk.Tk()
ventana.title("Cálculo de Aceleración")
ventana.geometry("400x400")
ventana.resizable(False, False)

lbl_masa = tk.Label(ventana, text="Masa (kg):")
lbl_masa.pack()
entry_masa = tk.Entry(ventana)
entry_masa.pack()

lbl_coef_friccion = tk.Label(ventana, text="Coeficiente de fricción:")
lbl_coef_friccion.pack()
entry_coef_friccion = tk.Entry(ventana)
entry_coef_friccion.pack()

lbl_grado_inclinacion = tk.Label(ventana, text="Grado de inclinación:")
lbl_grado_inclinacion.pack()
entry_grado_inclinacion = tk.Entry(ventana)
entry_grado_inclinacion.pack()

btn_calcular = tk.Button(ventana, text="Calcular Aceleración", command=calcular_aceleracion)
btn_calcular.pack()

lbl_resultado = tk.Label(ventana, text="Aceleración: ")
lbl_resultado.pack()

btn_grafico = tk.Button(ventana, text="Mostrar Gráfico", command=mostrar_grafico)
btn_grafico.pack()

btn_animacion = tk.Button(ventana, text="Mostrar Animación", command=mostrar_animacion)
btn_animacion.pack()

ventana.mainloop()