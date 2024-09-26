# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 12:22:47 2024

@author: Yessa
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

# Ruta de la carpeta que contiene los archivos CSV
carpeta = "C:\\Users\\Yessa\\OneDrive\\Documents\\mi_carpeta"
carpeta_salida = "C:\\Users\\Yessa\\OneDrive\\Documents\\mi_carpeta"

# Nombres de los archivos que quieres graficar
archivos = ["0.csv", "1.csv", "2.csv", "3.csv", "4.csv"]

# Iterar sobre cada archivo para generar las gráficas
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
    
    # Graficar los datos (aplicar un espaciado para mayor claridad)
    plt.figure(dpi=300)
    plt.plot(ejex[::10], datos[::10])  # Graficar 1 de cada 10 puntos para mayor claridad
    plt.title(f'Gráfica de {archivo}')
    plt.xlabel('Tiempo (ms)')
    plt.ylabel('Intensidad (mV)')
    plt.tight_layout()
    
    # Guardar la gráfica
    grafica_salida = archivo.replace('.csv', '.png')
    plt.savefig(os.path.join(carpeta_salida, grafica_salida))
    plt.show()
    
    print(f"Gráfica generada: {grafica_salida}")
