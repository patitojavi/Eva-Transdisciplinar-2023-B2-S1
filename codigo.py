import tkinter as tk 
import pygame

def abrir_ventana_pygame():
    pygame.init()
    pantalla = pygame.display.set_mode ((400, 300))
    pygame.display.set_caption("disp.pygame")

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
    pygame.quit()

ventana = tk.Tk()

ventana.title("pruebas de ventana")
ventana.geometry ("300x200")

boton = tk.Button(ventana, text="abrir ventana pygame", command= abrir_ventana_pygame)
boton.pack()

ventana.mainloop()   