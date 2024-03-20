import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.offline as py
py.init_notebook_mode(connected=True)
import plotly.graph_objs as go
import plotly.tools as tls
import seaborn as sns
import time
import os
import warnings
warnings.filterwarnings('ignore')

origen_co2 = pd.read_csv('C:/Users/josue/OneDrive/Escritorio/Josue/programas Python/PROYECTO_1/export_emissions.csv')
origen_co2 = origen_co2.iloc[0:64]
origen_co2.iloc[0][0]='Fecha'
origen_co2.columns = origen_co2.iloc[0]
origen_co2 = origen_co2[1:]
origen_co2 = origen_co2.set_index('Fecha')

origen_co2 = origen_co2.astype(float)
TOTAL_CO2_2022 = origen_co2.iloc[62].sum()
origen_co2.rename(columns={'Italy': 'Italia','Japan':'Japon','Russian Federation':'Rusia', 'Saudi Arabia': 
                            'Arabia Saudita', 'United States of America': 'Estados Unidos'}, inplace=True)

top_10_paises = ['China','Italia','Japon', 'India', 'Indonesia','Iran','Mexico','Rusia', 'Arabia Saudita', 'Estados Unidos']
origen_co2=pd.DataFrame(data=origen_co2, columns=top_10_paises)
origen_co2.drop_duplicates(inplace=True)

def ranking_mundial_co():
    Porcentaje = {}

    for index, value in enumerate(origen_co2.iloc[62]):
        Porcentaje[origen_co2.iloc[62].index[index]]= (value/TOTAL_CO2_2022)*100

    serie_datos= pd.Series(data=Porcentaje)
    serie_datos = serie_datos.sort_values(ascending=True)

    fig, ax = plt.subplots(figsize=(10,6))
    bars = ax.barh(serie_datos.index, serie_datos.values, color ='magenta')  
    ax.set_xlim(0, 100)

    # Agregar porcentajes de forma horizontal
    for bar in bars:
        width = bar.get_width()
        ax.text(width, bar.get_y() + bar.get_height() / 2, f'{width:.2f}%', va='center', ha='left')

    ax.set_xlabel('  ')
    ax.set_ylabel('    ')
    ax.set_title('Ranking mundial de los principales paises emisores\nde gases de efecto invernadero en 2022', fontweight=560,  fontstyle='oblique')

    # Guardar el gráfico de barras como archivo de imagen en el directorio 'static'
    nombre_archivo_barras = 'grafico_barras.png'
    ruta_archivo_barras = os.path.join('C:/Users/josue/OneDrive/Escritorio/Josue/programas Python/PROYECTO_1/static' , nombre_archivo_barras)
    plt.savefig(ruta_archivo_barras)
    plt.close()
    
    return ruta_archivo_barras
    
def co2_top3():
    years = np.unique(origen_co2.index)

    co2_china=[]
    co2_usa=[]
    co2_india=[]

    for year in years:
        co2_china.append(origen_co2[origen_co2.index == year]['China'].mean())
        co2_usa.append(origen_co2[origen_co2.index == year]['Estados Unidos'].mean())
        co2_india.append(origen_co2[origen_co2.index == year]['India'].mean())
        

    # Creamos la traza de china
    trace0 = go.Scatter(
        x = years, 
        y = co2_china,
        name='China',
        line=dict(
            color='rgb(0, 255, 255)',
        )
    )
    # Creamos la traza de india
    trace1 = go.Scatter(
        x = years, 
        y = co2_india,
        name='India',
        line=dict(
            color='rgb(255, 0, 255)',
        )
    )
    # Creamos la traza de Usa
    trace2 = go.Scatter(
        x = years, 
        y = co2_usa,
        name='Estados Unidos',
        line=dict(
            color='rgb(255, 255,0)',
        )
    )

    data = [trace0, trace1, trace2]

    layout = go.Layout(
        xaxis=dict(title='Año'),
        yaxis=dict(title='Medicion en Toneladas de CO2'),
        title='CO2 producidos por China, India y Estados Unidos', 
        showlegend = True)

    fig = go.Figure(data=data, layout=layout)
    #return py.iplot(fig)
    return py.plot(fig, output_type='div', include_plotlyjs=False)
