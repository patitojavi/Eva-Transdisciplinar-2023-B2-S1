import matplotlib.pyplot as plt
import numpy as np

# Coordenadas de los vértices del triángulo rectángulo
tx = [0, 6, 6, 0]
ty = [0, 0, 3, 0]

cx = [2.75, 3.20, 2, 1.50, 2.75]
cy = [2.40, 1.63, 1, 1.75, 2.40]

radio = 1.0
theta = np.linspace(0,np.pi,100)
cix = radio * np.cos(theta)
ciy = radio * np.sin(theta)

fig, ax = plt.subplots()

# Graficar el triángulo rectángulo
ax.plot(tx, ty)

# Graficar el cuadrado
ax.plot(cx, cy)

# graficar el circulo
ax.plot(cix, ciy)

#linea fuerza roce
ax.annotate('', xy=(4, 2.64), xytext=(2.30, 1.65),
            arrowprops=dict(arrowstyle='->'))

# linea fuerza normal
ax.annotate('', xy=(1.65, 2.90), xytext=(2.30, 1.65),
            arrowprops=dict(arrowstyle='->'))

# linea fuerza p
ax.annotate('', xy=(2.30, 0.30), xytext=(2.30, 1.65),
            arrowprops=dict(arrowstyle='->'))

plt.axis('equal')
plt.xlabel('Eje X')
plt.ylabel('Eje Y')
plt.title('plano inclinado')

# Mostrar el gráfico
plt.show()