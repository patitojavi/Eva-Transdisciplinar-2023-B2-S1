import tkinter as tk 
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def abrir_ventana_matplotlib():
    ventana_matplotlib = tk.Toplevel(ventana)
    ventana_matplotlib.title("Ventana de Matplotlib")
    ventana_matplotlib.geometry("400x300")

    # Crea una figura de Matplotlib
    figura = Figure(figsize=(5, 4), dpi=100)
    subplot = figura.add_subplot(111)
    subplot.plot([1, 2, 3, 4, 5], [1, 2, 3, 4, 5])

    # Crea un lienzo de Matplotlib en la ventana de Tkinter
    lienzo = FigureCanvasTkAgg(figura, master=ventana_matplotlib)
    lienzo.draw()
    lienzo.get_tk_widget().pack()

ventana = tk.Tk()
ventana.title("Pruebas de ventana")
ventana.geometry("300x200")

boton = tk.Button(ventana, text="Abrir ventana de Matplotlib", command=abrir_ventana_matplotlib)
boton.pack()

ventana.mainloop()  
