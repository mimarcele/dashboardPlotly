
# visit http://127.0.0.1:8050/ in your web browser.

from dash import Dash, html, dcc, Input, Output
import plotly.express as px
import pandas as pd

app = Dash(__name__)

df = pd.DataFrame({
    "Times": ["Flamengo", "Flamengo", "Flamengo", "Corinthians",  "Corinthians", "Corinthians", "Fluminense", "Fluminense", "Fluminense", "São Paulo"],
    "Gols": [20, 16, 30, 3, 9, 10, 0, 2, 8, 5],
    "Competições": ["Libertadores", "Copa do Brasil", "Brasileirão", "Libertadores", "Copa do Brasil", "Brasileirão", "Libertadores", "Copa do Brasil", "Brasileirão", "Brasileirão"]
})

fig = px.bar(df, x="Times", y="Gols", color="Competições", barmode="group")

app.layout = html.Div(children=[
    html.H1(children='Campeonatos 2019'),

    html.Div(children='''
        Dashboard Esportivo
    '''),


    dcc.Dropdown(
        id='dropdown',
        options=[
            {'label': 'Todos', 'value': 'Todos'},
            {'label': 'Flamengo', 'value': 'FLA'},
            {'label': 'Corinthians', 'value': 'SCCP'},
            {'label': 'Fluminense', 'value': 'FLU'},
            {'label': 'São Paulo', 'value': 'SPFC'}
        ],
        value='FLA',
    ),

    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])

@app.callback(
    Output(component_id='example-graph', component_property='figure'),
    Input(component_id='dropdown', component_property='value')
)
def changeText(value):
    if(value) == 'FLA':
        return px.bar(df[df['Times'] == 'Flamengo'], x="Times", y="Gols", color="Competições")
    elif(value) == 'FLU':
        return px.bar(df[df['Times'] == 'Fluminense'], x="Times", y="Gols", color="Competições")
    elif(value) == 'SCCP':
        return px.bar(df[df['Times'] == 'Corinthians'], x="Times", y="Gols", color="Competições")
    elif(value) == 'SPFC':
        return px.bar(df[df['Times'] == 'São Paulo'], x="Times", y="Gols", color="Competições")
    else:
        return px.bar(df, x="Times", y="Gols", color="Competições", barmode="group")


if __name__ == '__main__':
    app.run_server(debug=True)
