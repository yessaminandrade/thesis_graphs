# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 10:37:10 2024

@author: pepet
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#Importamos los datos
datos = pd.read_csv("prueba1.csv", header = None)
ejex = np.arange(0, 1000, 1)

#Graficamos 
plt.figure(dpi=300)
plt.plot(ejex, datos[0])
plt.show()

