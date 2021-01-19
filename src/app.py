import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output
import altair as alt
import pandas as pd
from vega_datasets import data


# Read in global data
movies = pd.read_json("data/raw/lab2-movies.json")
boom_movies = movies.explode('studios').explode('genres')

# Setup app and layout/frontend
app = dash.Dash(__name__,  external_stylesheets=['https://codepen.io/chriddyp/pen/bWLwgP.css'])
app.layout = html.Div([
    html.H1('MOVIE SELECTION APP', style = {'color': 'darkblue'}),
    html.P('A data visualization app that allows decision makers in the streaming companies to explore a dataset of movies to determine the popular movies that they need to provide to their users'),
    
    html.Iframe(
        id='genre-plot',
        style={'border-width': '0', 'width': '100%', 'height': '400px'}),
    dcc.Dropdown(
        id='xgenre-widget',
        value='Horror',  # REQUIRED to show the plot on the first page load
        options=[{'label': col, 'value': col} for col in boom_movies['genres'].unique()])])

# Set up callbacks/backend
@app.callback(
    Output('genre-plot', 'srcDoc'),
    Input('xgenre-widget', 'value'))
def plot_altair(xgenre):
    studios_by_revenue = boom_movies.groupby('studios')['revenue'].median().sort_values().index.tolist()
    
    chart= alt.Chart(boom_movies[boom_movies['genres']==xgenre]).mark_boxplot(color = "#20B2AA").encode(
        alt.X('vote_average'),
        alt.Y('studios', sort = studios_by_revenue),
        tooltip='title').interactive()
    return chart.to_html()
    

if __name__ == '__main__':
    app.run_server(debug=True)
