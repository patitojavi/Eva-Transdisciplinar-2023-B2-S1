import tkinter as tk
import math

class PlanoInclinadoApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Plano Inclinado")
        self.canvas = tk.Canvas(self, width=900, height=600)
        self.canvas.pack()
        self.create_plano_inclinado()
        self.create_objeto()
        self.animate_objeto()

    def create_plano_inclinado(self):
        self.canvas.create_line(200, 100, 600, 500, width=2)  # Línea inclinada del plano
        self.canvas.create_line(200, 100, 200, 500, 600, 500,width=2) 
       

    def create_objeto(self):
        x = 200
        y = 100
        self.objeto = self.canvas.create_oval(x, y, x + 50, y + 50, fill="red")

    def animate_objeto(self):
        x = 200
        y = 100
        angulo = math.atan2(500 - 100, 600 - 200)  # Calculamos el ángulo del plano (en radianes)
        velocidad = 5  # Velocidad constante del objeto

        while y < 500:
            vx = velocidad * math.cos(angulo)  # Componente horizontal de la velocidad
            vy = velocidad * math.sin(angulo)  # Componente vertical de la velocidad

            x += vx
            y += vy

            self.canvas.coords(self.objeto, x, y, x + 50, y + 50)  # Coordenadas de la forma ovalada
            self.update()
            self.after(50)

if __name__ == "__main__":
    app = PlanoInclinadoApp()
    app.mainloop()
