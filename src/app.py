import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output
import altair as alt
import pandas as pd
from vega_datasets import data
import dash_bootstrap_components as dbc

# Read in global data
movies = pd.read_json("data/raw/lab2-movies.json")
boom_movies = movies.explode('studios').explode('genres')

# Setup app and layout/frontend
app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])
app.layout = dbc.Container([
    html.H1('MOVIE SELECTION'),
    html.P('A data visualization app that allows decision makers in the streaming companies to explore a dataset of movies to determine the popular movies that they need to provide to their users'),
    dbc.Row([

        dbc.Col([
            
            dcc.Dropdown(
                    id='xgenre-widget',
                    value='Horror',  # REQUIRED to show the plot on the first page load
                    options=[{'label': col, 'value': col} for col in boom_movies['genres'].unique()]),
            
            html.Br(),
            html.Br(),

            dcc.RangeSlider(
                id = 'xbudget-widget',
                min = 10_000_000, max = 300_000_000, 
                value = [1_000_000, 2_000_000],
                marks = {10_000_000 : 'min', 300_000_000 : 'max'}),

            html.Br(),
            html.Br(),
            
            dbc.Card(
                        dbc.CardBody([
                            html.H6('Average box office value'),
                            html.H3('$123,238')
                        ]),
                        color='light'),

            html.Br(),
            html.Br(),

            dbc.Card(
                        dbc.CardBody([
                            html.H6('Average voting'),
                            html.H3('4.3')
                        ]),
                        color='light'),

            ],

            md=2),

        dbc.Col([
            dbc.Row([

                dbc.Col(html.Iframe(
                    id='genre-plot-1',
                    style={'border-width': '0', 'width': '150%', 'height': '300px'})
                    ),

                dbc.Col(html.Iframe(
                    id='genre-plot-2',
                    style={'border-width': '0', 'width': '150%', 'height': '300px'})
                    )

            ]),

            dbc.Row(html.Iframe(
                id='genre-plot-3',
                style={'border-width': '0', 'width': '100%', 'height': '300px'})
                ),
                
            dbc.Row(html.Iframe(
                id='genre-plot-4',
                style={'border-width': '0', 'width': '100%', 'height': '300px'})
                ) 
                
                ])

            ])
        ])



# Set up callbacks/backend

@app.callback(
    Output('genre-plot-1', 'srcDoc'),
    #[Input('xbudget-widget', 'value')],
    Input('xgenre-widget', 'value')
    )
def plot_altair(xgenre):  # to add xbudget later
    studios_by_revenue = boom_movies.groupby('studios')['revenue'].median().sort_values().index.tolist()
    #filtered_movies = boom_smovies.query('budget[0] < budget < budget[1]')
    chart= alt.Chart(boom_movies[boom_movies['genres']==xgenre]).mark_boxplot(color = "#20B2AA").encode(
        alt.X('vote_average'),
        alt.Y('studios', sort = studios_by_revenue),
        tooltip='title').interactive()
    return chart.to_html()


@app.callback(
    Output('genre-plot-2', 'srcDoc'),
    #[Input('xbudget-widget', 'value')],
    Input('xgenre-widget', 'value')
    )
def plot_altair(xgenre):  # to add xbudget later
    studios_by_revenue = boom_movies.groupby('studios')['revenue'].median().sort_values().index.tolist()
    #filtered_movies = boom_smovies.query('budget[0] < budget < budget[1]')
    chart= alt.Chart(boom_movies[boom_movies['genres']==xgenre]).mark_boxplot(color = "#20B2AA").encode(
        alt.X('vote_average'),
        alt.Y('studios', sort = studios_by_revenue),
        tooltip='title').interactive()
    return chart.to_html()



@app.callback(
    Output('genre-plot-3', 'srcDoc'),
    #[Input('xbudget-widget', 'value')],
    Input('xgenre-widget', 'value')
    )
def plot_altair(xgenre):  # to add xbudget later
    studios_by_revenue = boom_movies.groupby('studios')['revenue'].median().sort_values().index.tolist()
    #filtered_movies = boom_smovies.query('budget[0] < budget < budget[1]')
    chart= alt.Chart(boom_movies[boom_movies['genres']==xgenre]).mark_boxplot(color = "#20B2AA").encode(
        alt.X('vote_average'),
        alt.Y('studios', sort = studios_by_revenue),
        tooltip='title').interactive()
    return chart.to_html()



@app.callback(
    Output('genre-plot-4', 'srcDoc'),
    #[Input('xbudget-widget', 'value')],
    Input('xgenre-widget', 'value')
    )
def plot_altair(xgenre):  # to add xbudget later
    studios_by_revenue = boom_movies.groupby('studios')['revenue'].median().sort_values().index.tolist()
    #filtered_movies = boom_smovies.query('budget[0] < budget < budget[1]')
    chart= alt.Chart(boom_movies[boom_movies['genres']==xgenre]).mark_boxplot(color = "#20B2AA").encode(
        alt.X('vote_average'),
        alt.Y('studios', sort = studios_by_revenue),
        tooltip='title').interactive()
    return chart.to_html()

    

if __name__ == '__main__':
    app.run_server(debug=True)


# Notes
# 1. how to shorten call back
# 2. how to incorporate rangeslicer
# 3. formating card
# 4. overall aesthetic (esp left column)