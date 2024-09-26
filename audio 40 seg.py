# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 15:28:17 2024

@author: Yessa
"""

import pandas as pd
import numpy as np
import soundfile as sf
import os

# Ruta de la carpeta que contiene los archivos CSV
carpeta = "C:\\Users\\Yessa\\OneDrive\\Documents\\mi_carpeta"
carpeta_salida = "C:\\Users\\Yessa\\OneDrive\\Documents\\audios"

# Nombres de los archivos que quieres convertir a audio
archivos = ["0.csv", "1.csv", "2.csv", "3.csv", "4.csv"]

# Duración deseada para el audio (40 segundos)
duracion_deseada = 40  # Duración en segundos

# Frecuencia de muestreo arbitraria, puedes cambiarla
frecuencia_muestreo = 44100  # Usada para convertir a segundos, pero no es el foco principal

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
    
    # Ajustar la cantidad de puntos a la duración deseada
    num_puntos_original = len(datos_normalizados)
    num_puntos_deseado = duracion_deseada * frecuencia_muestreo  # Puntos necesarios para 40 segundos
    datos_redimensionados = np.interp(np.linspace(0, num_puntos_original, num_puntos_deseado),
                                      np.arange(num_puntos_original), datos_normalizados)
    
    # Generar el archivo de audio con la duración ajustada
    archivo_salida = os.path.join(carpeta_salida, archivo.replace(".csv", ".wav"))
    sf.write(archivo_salida, datos_redimensionados, frecuencia_muestreo)
    
    print(f"Archivo de audio generado con duración de 40 segundos: {archivo_salida}")
