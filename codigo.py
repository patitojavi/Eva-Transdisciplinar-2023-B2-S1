import math

def calcular_friccion(masa, angulo):
    if angulo > 35:
        aceleracion = 9.8 * math.sin(math.radians(angulo))
        friccion = masa * aceleracion
        return friccion
    else:
        return 0

def calcular():
    masa = float(masa_entry.get())
    angulo = float(angulo_entry.get())
    friccion = calcular_friccion(masa, angulo)
    resultado_label.config(text=f"La fricción es: {friccion} N")