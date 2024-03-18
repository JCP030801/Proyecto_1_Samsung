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

global_temp = pd.read_csv('C:/Users/josue/OneDrive/Escritorio/Josue/programas Python/PROYECTO_1/GlobalTemperatures.csv')
remove_columns= [
       'LandMaxTemperature', 'LandMaxTemperatureUncertainty',
       'LandMinTemperature', 'LandMinTemperatureUncertainty',
       'LandAndOceanAverageTemperature',
       'LandAndOceanAverageTemperatureUncertainty']

global_temp = global_temp.drop(remove_columns,axis=1)
global_temp.dropna(inplace=True)
global_temp= global_temp.rename(columns={'dt': 'Date'})
global_temp.drop_duplicates(inplace=True)

def temperatura_promedio_global():

    years = np.unique(global_temp['Date'].apply(lambda x: x[:4]))

    mean_temp_world = []
    mean_temp_world_uncertainty = []

    # Filtramos las filas del DataFrame donde los primeros cuatro caracteres de la columna 'Date' son iguales al año actual en la iteración.
    # Se calcula la media de la columna 'LandAverageTemperature' y 'LandAverageTemperatureUncertainty' para estas filas filtradas.
    for year in years:
        mean_temp_world.append(global_temp[global_temp['Date'].apply(
            lambda x: x[:4]) == year]['LandAverageTemperature'].mean())
        mean_temp_world_uncertainty.append(global_temp[global_temp['Date'].apply(
                    lambda x: x[:4]) == year]['LandAverageTemperatureUncertainty'].mean())
        
    # Creamos la traza que va por arriba de la temperatura promedio
    trace0 = go.Scatter(
        x = years, 
        y = np.array(mean_temp_world) + np.array(mean_temp_world_uncertainty),
        fill= None,
        mode='lines',
        name='Uncertainty top',
        line=dict(
            color='rgb(0, 255, 255)',
        )
    )
    # Creamos la traza que va por debajo de la temperatura promedio
    trace1 = go.Scatter(
        x = years, 
        y = np.array(mean_temp_world) - np.array(mean_temp_world_uncertainty),
        fill='tonexty',
        mode='lines',
        name='Uncertainty bot',
        line=dict(
            color='rgb(0, 255, 255)',
        )
    )
    # Creamos la traza de la temperatura promedio
    trace2 = go.Scatter(
        x = years, 
        y = mean_temp_world,
        name='Average Temperature',
        line=dict(
            color='rgb(199, 121, 093)',
        )
    )

    data = [trace0, trace1, trace2]

    layout = go.Layout(
        xaxis=dict(title='Año'),
        yaxis=dict(title='Temperatura promedio, °C'),
        title='Temperatura promedio en el mundo',
        showlegend = False)

    fig = go.Figure(data=data, layout=layout)
    return py.plot(fig, output_type='div', include_plotlyjs=False)