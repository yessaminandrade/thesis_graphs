# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 07:53:26 2024

@author: Yessa
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Paso 1: Leer el archivo Excel y limitar a las filas y columnas deseadas
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

# Paso 5: Graficar la señal original (X vs Y)
plt.figure(figsize=(10, 6))

plt.subplot(2, 1, 1)
plt.plot(x, y)
plt.title('Gráfico de X vs Y')
plt.xlabel('X')
plt.ylabel('Y')

# Paso 6: Graficar la Transformada de Fourier de Y
plt.subplot(2, 1, 2)
plt.plot(frecuencias, np.abs(transformada_y))
plt.title('Transformada de Fourier de Y')
plt.xlabel('Frecuencia [Hz]')
plt.ylabel('Amplitud')

plt.tight_layout()
plt.show()
