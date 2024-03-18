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
import os
warnings.filterwarnings('ignore')

from flask import Flask, render_template
from Modulo_1 import generar_mapa_global, generar_temp_promedio
from Modulo_2 import temperatura_promedio_global
from Modulo_3 import ranking_mundial_co, co2_top3
from Modulo_4 import origen_co2

app = Flask(__name__)

@app.route('/')
def index():
    
    folder_path = 'static'
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    
    graph_html1 = generar_mapa_global()
    graph_html2 = generar_temp_promedio()
    graph_html3 = temperatura_promedio_global()
    ranking_mundial_co()
    origen_co2()
    graph_html5 = co2_top3()
    nombre_archivo_barras = 'grafico_barras.png'
    nombre_archivo_barras_2 = 'grafico_barras_2.png'
    return render_template('index.html', graph_html1=graph_html1, graph_html2=graph_html2, 
                           graph_html3=graph_html3, graph_html4=nombre_archivo_barras, 
                           graph_html5=graph_html5, graph_html6=nombre_archivo_barras_2
                           )

if __name__ == '__main__':
    app.run(debug=True)
