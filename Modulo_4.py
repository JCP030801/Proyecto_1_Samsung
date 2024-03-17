import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.offline as py
py.init_notebook_mode(connected=True)
import plotly.graph_objs as go
import plotly.tools as tls
import seaborn as sns
import time
import warnings
warnings.filterwarnings('ignore')

fuentes_co2 = pd.read_excel('archivo.xlsx', index_col=0, engine='openpyxl')
fuentes_co2.drop_duplicates(inplace=True)

def origen_co2():
    
    plt.figure(figsize=(20, 6))
    plt.xlim(1959,2022)

    # Graficar cada columna
    for column in fuentes_co2.columns:
        plt.plot(fuentes_co2.index, fuentes_co2[column], marker='o', label=column)

    # Rellenar el área bajo las lineas con el mismo color
    plt.fill_between(fuentes_co2.index, fuentes_co2.min(axis=1), fuentes_co2.max(axis=1), color='lightseagreen', alpha=0.3)
    plt.fill_between(fuentes_co2.index, fuentes_co2['Cemento'], color='lightseagreen', alpha=0.3)


    plt.title('Evolución en las emisiones globales de CO2 por origen', fontsize=18)
    plt.xlabel('Año')
    plt.ylabel('Toneladas de CO2 (Miles de millones)')
    plt.legend()

    plt.grid(True) # Mostrar la cuadrícula
    plt.show()