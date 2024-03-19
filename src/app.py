from dash import Dash, html, dash_table, dcc, callback, Output, Input
import pandas as pd
import plotly.express as px

#incorporate data
df = pd.read_csv("violence_dashboard\\NIBRS_ARRESTEE.csv")

app = Dash(__name__)

app.layout = html.Div([
    html.Div(children='My First App with Data and Graph'),
    html.Hr(),
    dcc.RadioItems(options=['race_id','sex_code','age_num'], value = 'race_id', id='controls-and-radio-item'),
    dash_table.DataTable(data = df.to_dict("records"),page_size = 30),
    #dcc.Graph(figure = px.histogram(df, x="offense_code", y="age_num", histfunc = "avg"))
    dcc.Graph(figure={},id = 'controls-and-graph')
])

@callback(
    Output(component_id='controls-and-graph', component_property='figure'),
    Input(component_id='controls-and-radio-item', component_property = 'value')
)

def update_graph(col_chosen):
    fig = px.histogram(df, x='offense_code', y=col_chosen, histfunc = 'avg')
    return fig

if __name__ == '__main__':
    app.run(debug=True)