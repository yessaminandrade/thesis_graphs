# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 08:48:05 2024

@author: Yessa
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import soundfile as sf
import os

# Ruta de la carpeta que contiene el archivo de Excel
carpeta = r"C:\Users\Yessa\OneDrive\Documents\output_file"
carpeta_salida = r"C:\Users\Yessa\OneDrive\Documents\output_file"

# Nombre del archivo de Excel que quieres convertir a audio
archivo = "pedro.xlsx"

# Crear la ruta completa del archivo de Excel
ruta_completa = os.path.join(carpeta, archivo)

# Verifica si el archivo existe en la ruta dada
if not os.path.exists(ruta_completa):
    print(f"El archivo no se encuentra en la ruta: {ruta_completa}")
else:
    # Leer los datos del archivo de Excel, usar la cuarta y quinta columna como X_values e Y_values
    data = pd.read_excel(ruta_completa, usecols=[3, 4], nrows=2500, header=None)
    
    # Extraer las señales X e Y
    x_values = data[3].values.astype(float)
    y_values = data[4].values.astype(float)
    
    # Crear la gráfica
    plt.plot(x_values, y_values)
    plt.title('Señal Original del Osciloscopio')
    plt.xlabel('Tiempo')
    plt.ylabel('Amplitud')
    plt.show()
    
    # Generar el archivo de audio directamente sin cambiar la frecuencia de muestreo
    archivo_salida = os.path.join(carpeta_salida, archivo.replace(".xlsx", ".wav"))
    sf.write(archivo_salida, y_values.astype(np.float32), len(y_values))
    print(f"Archivo de audio generado: {archivo_salida}")