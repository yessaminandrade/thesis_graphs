# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 10:06:47 2024

@author: Yessa
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Paso 1: Leer el archivo Excel
archivo = "C:/Users/Yessa/OneDrive/Documents/output_file/pancho.xlsx"
datos = pd.read_excel(archivo)

# Paso 2: Extraer los datos de las columnas 4 y 5 (X e Y) y de las filas 1 a 2500
x = datos.iloc[0:2500, 3]  # Columna 4 como X (indexada en 3)
y = datos.iloc[0:2500, 4]  # Columna 5 como Y (indexada en 4)

# Paso 3: Eliminar las filas con valores nulos en ambas columnas para que tengan el mismo tamaño
datos_limpios = datos.iloc[0:2500, [3, 4]].dropna()

x = datos_limpios.iloc[:, 0]  # Columna X limpia
y = datos_limpios.iloc[:, 1]  # Columna Y limpia

# Verificar si hay datos
print("Datos X (primeros 10 valores):", x.head(10))
print("Datos Y (primeros 10 valores):", y.head(10))

# Paso 4: Aplicar la Transformada de Fourier a Y
frecuencias = np.fft.fftfreq(len(y), d=1.0)  # Cambia d si conoces el intervalo de muestreo
transformada_y = np.fft.fft(y)

# --- Opciones de visualización mejorada ---

# Opción 1: Graficar la Transformada de Fourier con límites en el eje Y para hacer zoom
plt.figure(figsize=(10, 6))

plt.subplot(3, 1, 1)
plt.plot(x, y)
plt.title('Gráfico de X vs Y')
plt.xlabel('X')
plt.ylabel('Y')

# Opción 2: Graficar la Transformada de Fourier con límites en el eje Y para hacer zoom
plt.subplot(3, 1, 2)
plt.plot(frecuencias, np.abs(transformada_y))
plt.ylim(0, 500)  # Ajusta el valor para hacer zoom en los picos pequeños
plt.title('Transformada de Fourier de Y (Zoom en amplitudes pequeñas)')
plt.xlabel('Frecuencia [Hz]')
plt.ylabel('Amplitud (Zoom)')

# Opción 3: Graficar la Transformada de Fourier con escala logarítmica en el eje Y
plt.subplot(3, 1, 3)
plt.plot(frecuencias, np.abs(transformada_y))
plt.yscale('log')
plt.title('Transformada de Fourier de Y (Escala Logarítmica)')
plt.xlabel('Frecuencia [Hz]')
plt.ylabel('Amplitud (Escala Logarítmica)')

plt.tight_layout()
plt.show()




