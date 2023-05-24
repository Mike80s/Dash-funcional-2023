import dash
from dash import dcc
from dash import html
import plotly
import random
import plotly.graph_objs as go
from collections import deque

import pandas as pd

# Visualisation
import seaborn as sns
import plotly.express as px
# from callbacks import register_callbacks
import plotly.graph_objects as go

# df = pd.read_csv("data.csv")
df = pd.read_csv("data.csv", encoding="ISO-8859-1")

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
# fig= px.bar(df, x='Tiene internet en casa', y='Puntaje global')
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server=app.server
app.layout = html.Div([
    html.H1(children="Análisis de las pruebas Saber 11 año 2020"),
    dcc.Graph(figure=px.histogram(df, x='Tiene internet en casa'))
])

# def update_output_div(input_value):
# return 'you wrote"{}"'.format(input_value)

if __name__ == '__main__':
    app.run_server(debug=False)
