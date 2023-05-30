# Configuración de la ventana principal
ventana = tk.Tk()
ventana.title("Cálculo de Fricción")
ventana.geometry("400x300")

# Creación de los elementos de la interfaz de usuario
masa_label = tk.Label(ventana, text="Masa (kg):")
masa_label.pack()
masa_entry = tk.Entry(ventana)
masa_entry.pack()

angulo_label = tk.Label(ventana, text="Ángulo (grados):")
angulo_label.pack()
angulo_entry = tk.Entry(ventana)
angulo_entry.pack()

calcular_button = tk.Button(ventana, text="Calcular", command=calcular)
calcular_button.pack()

resultado_label = tk.Label(ventana, text="")
resultado_label.pack()


# Bucle principal de la aplicación
ventana.mainloop()