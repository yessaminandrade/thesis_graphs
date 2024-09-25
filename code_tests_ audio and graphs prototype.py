# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import soundfile as sf
import os

# Ruta de la carpeta que contiene los archivos CSV
carpeta = "C:\\Users\\Yessa\\OneDrive\\Documents\\mi_carpeta"
carpeta_salida = "C:\\Users\\Yessa\\OneDrive\\Documents\\mi_carpeta"

# Nombres de los archivos que quieres convertir a audio
archivos = ["0.csv", "1.csv", "2.csv", "3.csv", "4.csv"]

# Frecuencia de muestreo utilizada por el osciloscopio (ajústala si la conoces)
frecuencia_muestreo = 44100  # 44.1 kHz (calidad de CD, ajusta según tu osciloscopio)

# Iterar sobre cada archivo para generar las gráficas y convertir los datos a audio
for archivo in archivos:
    ruta_completa = os.path.join(carpeta, archivo)  # Crear la ruta completa del archivo CSV
    datos = pd.read_csv(ruta_completa, header=None)  # Leer el archivo CSV
    
    # Filtrar los datos a partir de la cuarta fila y convertir a numérico
    datos = datos[0][3:].apply(pd.to_numeric, errors='coerce')  # Usar filas desde la cuarta fila en adelante
    
    if len(datos) == 0:
        print(f"El archivo {archivo} no tiene suficientes datos útiles.")
        continue
    
    # Crear el eje X (tiempo en milisegundos)
    ejex = np.arange(0, len(datos), 1)  # Eje X como tiempo en milisegundos
    
    # Graficar los datos
    plt.figure(dpi=300)
    plt.plot(ejex, datos)
    plt.title(f'Gráfica de {archivo}')
    plt.xlabel('Tiempo (ms)')
    plt.ylabel('Intensidad (mV)')
    plt.tight_layout()
    
    # Guardar la gráfica si deseas
    grafica_salida = archivo.replace('.csv', '.png')
    plt.savefig(os.path.join(carpeta_salida, grafica_salida))
    plt.show()
    
    # Normalizar los datos para que estén en el rango de -1 a 1
    datos_normalizados = datos / np.max(np.abs(datos))
    
    # Guardar el archivo de audio
    archivo_salida = os.path.join(carpeta_salida, archivo.replace(".csv", ".wav"))
    sf.write(archivo_salida, datos_normalizados, frecuencia_muestreo)
    
    print(f"Gráfica y archivo de audio generados: {grafica_salida}, {archivo_salida}")
