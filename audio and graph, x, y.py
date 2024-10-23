import pandas as pd
import numpy as np
import soundfile as sf
import os
import matplotlib.pyplot as plt

# Ruta de la carpeta que contiene el archivo de Excel
carpeta = r"C:\Users\Yessa\OneDrive\Documents\output_file"
carpeta_salida = r"C:\Users\Yessa\OneDrive\Documents\output_file"

# Nombre del archivo de Excel que quieres convertir a audio
archivo = "pancho.xlsx"

# Frecuencia de muestreo original
frecuencia_original = 75  # Ajusta esto si es necesario

# Crear la ruta completa del archivo de Excel
ruta_completa = os.path.join(carpeta, archivo)

# Verifica si el archivo existe en la ruta dada
if not os.path.exists(ruta_completa):
    print(f"El archivo no se encuentra en la ruta: {ruta_completa}")
else:
    # Leer los datos del archivo de Excel, usar la cuarta y quinta columna como X_values e Y_values
    data = pd.read_excel(ruta_completa, usecols=[3, 4], nrows=2500, header=None)
    
    # Extraer la señal Y
    y_values = data[4].values.astype(float)  # Asegurarse de que los datos son float
    
    # Visualizar la señal original
    plt.plot(y_values)
    plt.title('Señal Original del Osciloscopio')
    plt.xlabel('Muestras')
    plt.ylabel('Amplitud')
    plt.show()
    
    # Normalizar los valores de Y para adaptarlos a la amplitud del audio (-1 a 1)
    y_values_normalizados = np.interp(y_values, (y_values.min(), y_values.max()), (-1, 1))
    
    # Frecuencia de muestreo de salida para el archivo de audio (44.1 kHz es estándar para audio)
    frecuencia_salida_audio = 44100
    
    # Ajustar la cantidad de puntos para que el audio mantenga la forma original pero caiga en el rango audible
    factor_temporal = frecuencia_salida_audio / frecuencia_original
    y_values_reescalados = np.interp(np.arange(0, len(y_values_normalizados) * factor_temporal),
                                     np.arange(len(y_values_normalizados)),
                                     y_values_normalizados)
    
    # Generar el archivo de audio
    archivo_salida = os.path.join(carpeta_salida, archivo.replace(".xlsx", ".wav"))
    sf.write(archivo_salida, y_values_reescalados.astype(np.float32), frecuencia_salida_audio)
    print(f"Archivo de audio generado: {archivo_salida}")

