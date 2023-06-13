import matplotlib.pyplot as plt

# Crear el gráfico
fig, ax = plt.subplots()

# Graficar un punto de referencia
ax.plot(0, 0, 'ro')

# Agregar el texto
ax.text(0, 0, 'A', fontsize=12, ha='center', va='center')

# Configurar el gráfico
plt.xlabel('Eje X')
plt.ylabel('Eje Y')
plt.title('Letra en el Gráfico')

# Mostrar el gráfico
plt.show()