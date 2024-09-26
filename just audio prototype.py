# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 12:27:11 2024

@author: Yessa
"""

import pandas as pd
import numpy as np
import soundfile as sf
import os

# Ruta de la carpeta que contiene los archivos CSV
carpeta = "C:\\Users\\Yessa\\OneDrive\\Documents\\mi_carpeta"
carpeta_salida = "C:\\Users\\Yessa\\OneDrive\\Documents\\mi_carpeta"

# Nombres de los archivos que quieres convertir a audio
archivos = ["0.csv", "1.csv", "2.csv", "3.csv", "4.csv"]

# Frecuencia de muestreo original (ajusta si la conoces)
frecuencia_muestreo = 44100  # 44.1 kHz por defecto, ajusta según el osciloscopio

# Multiplicador de tiempo (ajusta este valor para alargar o acortar el audio)
multiplicador_tiempo = 10  # Por ejemplo, multiplicar el tiempo por 10 para que el audio dure más

# Iterar sobre cada archivo para convertir los datos a audio
for archivo in archivos:
    ruta_completa = os.path.join(carpeta, archivo)  # Crear la ruta completa del archivo CSV
    datos = pd.read_csv(ruta_completa, header=None)  # Leer el archivo CSV
    
    # Filtrar los datos a partir de la cuarta fila y convertir a numérico
    datos = datos[0][3:].apply(pd.to_numeric, errors='coerce')  # Usar filas desde la cuarta fila en adelante
    
    if len(datos) == 0:
        print(f"El archivo {archivo} no tiene suficientes datos útiles.")
        continue
    
    # Normalizar los datos para que estén en el rango de -1 a 1
    datos_normalizados = datos / np.max(np.abs(datos))
    
    # Ajustar la frecuencia de muestreo con el multiplicador de tiempo
    nueva_frecuencia_muestreo = frecuencia_muestreo // multiplicador_tiempo
    
    # Generar el archivo de audio usando la frecuencia de muestreo ajustada
    archivo_salida = os.path.join(carpeta_salida, archivo.replace(".csv", ".wav"))
    sf.write(archivo_salida, datos_normalizados, nueva_frecuencia_muestreo)
    
    print(f"Archivo de audio generado: {archivo_salida}")
