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

global_temp_country = pd.read_csv('C:/Users/josue/OneDrive/Escritorio/Josue/programas Python/PROYECTO_1/GlobalLandTemperaturesByCountry.csv')
global_temp_country.dropna(inplace=True)
global_temp_country= global_temp_country.rename(columns={'dt': 'Date'})
global_temp_country.drop_duplicates(inplace=True)

global_temp_country = global_temp_country[~global_temp_country['Country'].isin(
    ['Denmark', 'Antarctica', 'France', 'Europe', 'Netherlands',
     'United Kingdom', 'Africa', 'South America'])]

global_temp_country = global_temp_country.replace(
   ['Denmark (Europe)', 'France (Europe)', 'Netherlands (Europe)', 'United Kingdom (Europe)'],
   ['Denmark', 'France', 'Netherlands', 'United Kingdom'])


def generar_mapa_global():
    
    countries = np.unique(global_temp_country['Country'])
    mean_temp = []
    # Este bucle calcula la temperatura promedio para cada país en la lista countries y almacena estos valores en una lista llamada mean_temp.
    for country in countries:
        mean_temp.append(global_temp_country[global_temp_country['Country'] == country]['AverageTemperature'].mean())


    # Creando un choropleth map
    data = [ dict(
            type = 'choropleth',
            locations = countries,
            z = mean_temp,
            locationmode = 'country names',
            text = countries,
            marker = dict(
                line = dict(color = 'rgb(0,0,0)', width = 1)),
                colorbar = dict( tickprefix = '', 
                title = 'Temperatura\nPromedio,\n°C')
                )
        ]

    layout = dict(
        title = '',#Temperatura promedio en todos los paises
        geo = dict(
            showframe = False,
            showocean = True,
            oceancolor = 'rgb(0,255,255)',
            projection = dict(
            type = 'orthographic',
                rotation = dict(
                        lon = 60,
                        lat = 10),
            ),
            lonaxis =  dict(
                    showgrid = True,
                    gridcolor = 'rgb(102, 102, 102)'
                ),
            lataxis = dict(
                    showgrid = True,
                    gridcolor = 'rgb(102, 102, 102)'
                    )
                ),
            )

    fig = dict(data=data, layout=layout)
    return py.plot(fig, output_type='div', include_plotlyjs=False)


######

def generar_temp_promedio():
    
    continent = ['Russia', 'United States', 'Dominican Republic', 'Canada', 'Bolivia', 'China']
    
    years = np.unique(global_temp_country['Date'].apply(lambda x: x[:4]))
    years = list(map(int,years))

    # Eliminar todos los datos menores a 1850
    years = [x for x in years if x >= 1850]
    years = list(map(str, years))


    mean_temp_year_country = [ [0] * len(years[5:]) for i in range(len(continent))]

    j = 0
    for country in continent:
        all_temp_country = global_temp_country[global_temp_country['Country'] == country]
        i = 0
        for year in years[5:]:
            mean_temp_year_country[j][i] = all_temp_country[all_temp_country['Date'].apply(
                    lambda x: x[:4]) == year]['AverageTemperature'].mean()
            i +=1
        j += 1

    traces = []
    colors = ['rgb(0, 255, 255)', 'rgb(255, 0, 255)', 'rgb(0, 0, 0)',
            'rgb(255, 0, 0)', 'rgb(0, 255, 0)', 'rgb(0, 0, 255)']
    for i in range(len(continent)):
        traces.append(go.Scatter(
            x=years[5:],
            y=mean_temp_year_country[i],
            mode='lines',
            name=continent[i],
            line=dict(color=colors[i]),
        ))

    layout = go.Layout(
        xaxis=dict(title='Año'),
        yaxis=dict(title='Temperatura promedio, °C'),
        title='Tendencias de las Temperaturas en Países Clave',)

    fig = go.Figure(data=traces, layout=layout)
    return py.plot(fig, output_type='div', include_plotlyjs=False)

