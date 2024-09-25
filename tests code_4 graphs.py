import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os

# Ruta de la carpeta que contiene los archivos CSV
carpeta = "C:\\Users\\Yessa\\OneDrive\\Documents\\mi_carpeta"

# Nombres de los archivos que quieres graficar
archivos = ["1.csv", "2.csv", "3.csv", "4.csv"]

# Iterar sobre cada archivo y graficarlo
for archivo in archivos:
    ruta_completa = os.path.join(carpeta, archivo)  # Crear la ruta completa del archivo
    datos = pd.read_csv(ruta_completa, header=None)  # Leer el archivo CSV
    
    # Convertir los datos a números, forzando cualquier valor no numérico a NaN
    datos = datos.apply(pd.to_numeric, errors='coerce')
    
    # Crear el eje X en milisegundos
    ejex = np.arange(0, 1000, 1)
    
    # Graficar a partir de la cuarta fila (ignoramos las tres primeras filas)
    if len(datos) >= 1003:  # Asegúrate de que haya al menos 1003 filas (1000 datos + 3 filas inútiles)
        datos_filtrados = datos[0][3:1003]  # Usamos solo los datos útiles (de la cuarta fila en adelante)
        
        # Obtener los valores mínimos y máximos de los datos para el eje Y
        y_min = datos_filtrados.min()
        y_max = datos_filtrados.max()
        
        # Agregar un margen del 10% al mínimo y máximo para que no estén justo en los bordes
        margen = 0.1 * (y_max - y_min)
        y_min -= margen
        y_max += margen
        
        # Graficar
        plt.figure(dpi=300)
        plt.plot(ejex, datos_filtrados)  # Graficamos los datos desde la cuarta fila
        
        # Establecer los límites del eje Y usando los valores calculados
        plt.ylim(y_min, y_max)
        
        # Agregar etiquetas de los ejes
        plt.title(f'Gráfica de {archivo}')
        plt.xlabel('Tiempo (ms)')
        plt.ylabel('Intensidad (mV)')
        
        # Ajuste automático del diseño
        plt.tight_layout()
        
        plt.show()
    else:
        print(f"El archivo {archivo} no tiene suficientes datos útiles para graficar.")
