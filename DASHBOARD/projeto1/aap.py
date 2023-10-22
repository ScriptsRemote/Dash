# importando as bibliotecas
import dash
from dash import html, dcc
import plotly.express as px 
import pandas as pd

#instancias nosso dash
app = dash.Dash(__name__)

##Dataframe
df = pd.DataFrame(
    {
    'Cidade': ['São Gabriel', 'São Gabriel', 'São Gabriel', 'Agudo', 'Agudo', 'Agudo', 'Bagé', 'Bagé', 'Bagé'],
    'Estacao': ['Outono', 'Primavera', 'Verão','Primavera', 'Verão','Outono','Primavera', 'Verão','Outono'],
    'Temperatura': [14.8340, 23.0424, 30.2476, 32.3194, 28.9123, 18.1185, 21.3949, 34.9214, 16.6636]
})

##Driando um gráfico 
fig = px.bar(df, x='Estacao', y='Temperatura', color='Cidade')

#=======================Layout===========================
#usar o dash html components
##Primeiro criamos uma 'caixa' com a div e estabelecemos os componentes
app.layout = html.Div(id='div1',
    ##'filhos' da div
    children=[
        ##Criando uma tag de título começa em H1 e vai até H6
        html.H1('DashBoard Temperatura', id='h1'),
        
        html.Div('Dash:WebPython'),
        
        ##Acessar dashcorecomponents (gráficos, tabelas )
        dcc.Graph(figure=fig, id='graph')
    ]
    
)

##Encerrando o código
if __name__ =='__main__':
    app.run_server(debug=True, port=5050)