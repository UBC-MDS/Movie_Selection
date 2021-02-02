import dash
import dash_table as dt
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output
import altair as alt
import pandas as pd
import dash_bootstrap_components as dbc
import plotly.express as px
import plotly.io as pio
import plotly.graph_objects as go

pio.templates.default = 'simple_white'


# Read in global data
movies = pd.read_csv("data/processed/movies.csv")

# Setup app and layout/frontend
app = dash.Dash(external_stylesheets=[dbc.themes.LUMEN])
server = app.server

SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "20rem",
    "padding": "2rem 1rem",
    "z-index": 4000000
}

CONTENT_STYLE = {
    "margin-left": "20rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
    "z-index": -1
}


cards = dbc.CardDeck(
    [
        dbc.Card(
            dbc.CardBody(
                [
                    html.H6("Average Profit", className='card-title'),
                    html.H4(id='average-profit', className='card-text')
                ]
            ),
            color='primary',
            outline=True
        ),
        dbc.Card(
            dbc.CardBody(
                [
                    html.H6("Average box office value", className='card-title'),
                    html.H4(id="average-revenue", className='card-text'),
                ]
            ),
            color="primary",
            outline=True,
        ),
        dbc.Card(
            dbc.CardBody(
                [
                    html.H6("Average voting", className='card-title'), 
                    html.H4(id="average-vote", className='card-text')]
            ),
            color="primary",
            outline=True
        ),
        dbc.Card(
            dbc.CardBody(
                [
                    html.H6("Vote Count", className='card-title'),
                    html.H4(id='vote-count', className='card-text')
                ]
            ),
            color='primary',
            outline=True
        ),
    ]
)


genre_graphs = dbc.CardDeck([
    dbc.Card(
        [dbc.CardHeader(
            html.H4(id="vote-plot-title")
        ),
        dbc.CardBody(
            dcc.Graph(
                id='vote-plot',
            )
        )], 
        color="success",
        outline=True
    ),
    dbc.Card(
        [dbc.CardHeader(
            html.H4(id="revenue-plot-title")
        ),
        dbc.CardBody(
            dcc.Graph(
                id="revenue-plot"
            )
        )],
        color="success",
        outline=True
    )
])

studio_graphs = html.Div([
    dbc.Row([
        dbc.Col(
            dbc.Card(
                [
                dbc.CardHeader(
                    html.H4(id="vote-scatter-title")
                ),
                dbc.CardBody(
                    dcc.Graph(
                        id="vote-scatter-plot",
                    )
                )],
                color="info",
                outline=True
            ), 
        )
    ]),
    html.Br(),
    html.Br(),
    dbc.Row([
        dbc.Col(
            dbc.Card(
                [
                    dbc.CardHeader(
                        html.H4(id="table-title")
                    ),
                    dbc.CardBody(
                        html.Div(
                            id="movies-data-frame"
                        )
                    )
                ]
                ,
                color="info",
                outline=True
            )
        )
    ])
])

content = html.Div([
    cards,
    html.Br(),
    html.Br(),
    genre_graphs,
    html.Br(),
    html.Br(),
    studio_graphs
], id="page-content", style=CONTENT_STYLE)

controls = dbc.Card(
    [
        dbc.FormGroup(
            [
                dbc.Label("Genre"),
                dcc.Dropdown(
                    id="xgenre-widget",
                    value="Horror",  # REQUIRED to show the plot on the first page load
                    options=[
                        {"label": col, "value": col}
                        for col in movies["genres"].unique()
                    ],
                    clearable=False
                ),
            ]
        ),
        dbc.FormGroup(
            [
                dbc.Label("Budget Range (US$ mil)"),
                dcc.RangeSlider(
                    id="xbudget-widget",
                    min=10,
                    max=300,
                    value=[10, 300],
                    marks={
                        10: "10",
                        100: "100",
                        200: "200",
                        300: "300",
                    },
                ),
            ]
        ),
    ],
    body=True,
    className="text-dark"
)

sidebar = html.Div(
    [
        html.H2("Movie Selection", className="display-4"),
        html.Hr(),
        controls,
        html.Hr(),
        html.P(
            "A data visualization app that allows decision makers in the streaming companies to explore a dataset of movies to determine the popular movies that they need to provide to their users",
            className="lead"
        ),
    ],
    style=SIDEBAR_STYLE,
    className='bg-primary text-white'
)
app.layout = html.Div([sidebar, content])

# Set up callbacks/backend

@app.callback(
    Output("vote-plot", "figure"),
    Output("revenue-plot", "figure"),
    Output("vote-scatter-plot", "figure"),
    Output("average-revenue", "children"),
    Output("vote-plot-title", 'children'),
    Output("revenue-plot-title", 'children'),
    Output("vote-scatter-title", 'children'),
    Output("table-title", 'children'),
    Output("average-vote", "children"),
    Output("vote-count", "children"),
    Output("average-profit", "children"),
    Output("movies-data-frame", "children"),
    Input("xgenre-widget", "value"),
    Input("xbudget-widget", "value"),
    Input('revenue-plot', 'selectedData'),
    Input('vote-plot', 'selectedData')
)
def plot_altair(xgenre, budget, revenue_selected, vote_selected):  # to add xbudget later
    studios_by_revenue = (
        movies.groupby("studios")["revenue"].median().sort_values().index.tolist()
    )
    filtered_movies = movies[movies["genres"] == xgenre].query(
        "@budget[0] < budget and budget < @budget[1]"
    )

    # Cards
    average_revenue = "US${:,.2f} mil".format(filtered_movies["revenue"].mean())
    average_profit = "US${:,.2f} mil".format(filtered_movies["profit"].mean())
    average_vote = str(round(filtered_movies["vote_average"].mean(), 1))
    vote_count = str(round(filtered_movies['vote_count'].mean(), 1))

    # Genre graphs



    vote_chart = px.box(filtered_movies, x='vote_average', y = 'studios')
    vote_chart.add_bar(x=[filtered_movies.vote_average.max()] * filtered_movies.studios.nunique(), y = filtered_movies.studios.unique(), orientation='h', opacity=0.0001, hoverinfo='none', showlegend=False)
    vote_chart.update_layout(clickmode='event+select')
    revenue_chart = px.box(filtered_movies, x='revenue', y = 'studios')
    revenue_chart.add_bar(x=[filtered_movies.revenue.max()] * filtered_movies.studios.nunique(), y = filtered_movies.studios.unique(), orientation='h', opacity=0.0001, hoverinfo='none', showlegend=False)
    revenue_chart.update_layout(clickmode='event+select')

    studios_list = []

    if revenue_selected is not None:
        studios_list += [point['y'] for point in revenue_selected['points']]

    if vote_selected is not None:
        studios_list += [point['y'] for point in vote_selected['points']]

    if not studios_list:
        studios_list = filtered_movies.studios.unique()
    
    studio_movies = filtered_movies[filtered_movies['studios'].isin(studios_list)]
    vote_scatter_chart = px.scatter(studio_movies, x='vote_average', y='vote_count')

    top_movies_df = (studio_movies.nlargest(10, ["vote_average"]))[
        ["title", "vote_average", "profit", "runtime"]
    ]

    top_movies_df.profit = round(top_movies_df.profit, 3)
    top_movies_df.rename(
        columns={
            "title": "Title",
            "vote_average": "Vote Average",
            "profit": "Profit (US$ mil)",
            "runtime": "Runtime (min)",
        },
        inplace=True,
    )
    return (
        vote_chart,
        revenue_chart,
        vote_scatter_chart,
        average_revenue,
        f'{xgenre} Movies Vote Average By Studio',
        f'{xgenre} Movies Financials By Studio',
        f'Voting Profile For {xgenre} Movies',
        f'Most Popular {xgenre} Movies (By Vote Average)',
        average_vote,
        vote_count,
        average_profit,
        dbc.Table.from_dataframe(
                top_movies_df,
                striped=True,
                bordered=True,
                hover=True
        )
    )


if __name__ == "__main__":
    app.run_server(debug=True)