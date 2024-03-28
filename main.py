from dash import Dash, dcc, html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import pages
from app import app

navegacao = dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink("Gráficos", href="/graficos")),
        dbc.NavItem(dbc.NavLink("Formulário", href="/formulario")),
    ],
    brand="Dashboard de predição de doenças cardíacas",
    brand_href="/",
    color="dark",
    dark=True,
)

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    navegacao,
    html.Div(id='conteudo')
])

@app.callback(
    Output('conteudo', 'children'),
    [Input('url', 'pathname')]    
)
def mostrar_pagina(pathname):
    if pathname == '/formulario':
        return pages.form.layout
    elif pathname == '/graficos':
        return pages.graph.layout
    else:
        return html.P('Página inicial', className='text-center mb-5 custom-button')



app.run_server(debug=False, port=8050, host='0.0.0.0')
