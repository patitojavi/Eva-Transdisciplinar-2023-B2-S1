import pygame, sys
from tkinter import *
from pygame.locals import *

main_ventana = Tk()
main_ventana.title = ("Plano Inclinado")

ventana = Frame(main_ventana, width=1200, height=800)
ventana.pack()
pygame.init()

WIDTH, HEIGHT = 600, 400
ventanapy = pygame.display.set_mode((WIDTH, HEIGHT))    
line_y = HEIGHT // 2
line_width = WIDTH
line_color = (0, 0, 0)
square_size = 50
square_x = WIDTH - square_size
square_y = line_y - square_size // 2     
square_speed = 2

def draw():
    ventanapy.fill((255, 255, 255))
    pygame.draw.line(ventanapy, line_color, (0, line_y), (line_width, line_y), 10)
    pygame.draw.rect(ventanapy, (255, 0, 0), (square_x, square_y, square_size, square_size)) 
    pygame.display.flip()


def update_animation():
    global square_x
    square_x -= square_speed
    if square_x < -square_size:
        square_x = WIDTH
    draw()
    main_ventana.after(16, update_animation)


def cuadromasa():
    masa = Entry(ventana)
    masa.grid(row=0, column=1, padx =10, pady= 10)
    masa.config(fg="black", justify="right")
    masa_label = Label(ventana, text="Peso(Kg):")
    masa_label.grid(row=0, column=0, sticky="e", padx=10, pady=10)
    
def cuadroinclinacion():
    inclinacion = Entry(ventana)
    inclinacion.grid(row=1, column=1, padx =10, pady= 10)
    inclinacion.config(fg="black", justify="right")
    inclinacion_label = Label(ventana, text="Inclinación:")
    inclinacion_label.grid(row=1, column=0, sticky="e", padx=10, pady=10)

def cuadroroce():
    roce = Entry(ventana)
    roce.grid(row=2, column=1, padx =10, pady= 10)
    roce.config(fg="black", justify="right")
    roce_label = Label(ventana, text="Fuerza Roce:")
    roce_label.grid(row=2, column=0, sticky="e", padx=10, pady=10)
    botoncalcular = Button(ventana, text= "Calcular", command=ecuacionboton)
    botoncalcular.grid(column=0, columnspan=2, padx=10, pady=10)
    
    
def ecuacionboton():
    pass




update_animation()
cuadromasa()
cuadroinclinacion()
cuadroroce()
ventana.mainloop()