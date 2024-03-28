from ucimlrepo import fetch_ucirepo
import plotly.express as px
from dash import Dash, dcc, html
import dash_bootstrap_components as dbc

heart_disease = fetch_ucirepo(id=45)
dados = heart_disease.data.features
dados["doenca"] = (heart_disease.data.targets > 0) * 1

# Criando os gráficos iniciais
figura_histograma = px.histogram(dados, x='age')
div_do_histograma = html.Div([
            html.H3('Histograma de idades', className='text-center mt-2 custom-button'),
            dcc.Graph(figure=figura_histograma),
        ])

figura_boxplot = px.box(dados, x='doenca', y='age', color='doenca')
div_do_boxplot = html.Div([
            html.H3('Distribuição das idades', className='text-center custom-button'),
            dcc.Graph(figure=figura_boxplot)
        ])

# Adicionando os novos gráficos
figura_boxplot_chol = px.box(dados, x='doenca', y='chol', color='doenca')
div_do_boxplot_chol = html.Div([
            html.H3('Colesterol Sérico', className='text-center mt-5 custom-button'),
            dcc.Graph(figure=figura_boxplot_chol)
        ])

figura_boxplot_trestbps = px.box(dados, x='doenca', y='trestbps', color='doenca')
div_do_boxplot_trestbps = html.Div([
            html.H3('Pressão sanguínea em repouso', className='text-center mt-5 custom-button'),
            dcc.Graph(figure=figura_boxplot_trestbps)
        ])

# Organizando o layout
layout = html.Div([
        html.H1('Análise de dados do UCI Repository Heart Disease', className='text-center mb-5 mt-5 custom-title'),
        dbc.Container([
            dbc.Row([
                dbc.Col([div_do_histograma, div_do_boxplot_chol], md=6),
                dbc.Col([div_do_boxplot, div_do_boxplot_trestbps], md=6)
            ], align="start")
        ])
    ])