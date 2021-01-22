import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output
import altair as alt
import pandas as pd
import dash_bootstrap_components as dbc

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
                    html.H6("Average box office value", className='card-title'),
                    html.H4(id="average-revenue", className='card-text'),
                ]
            ),
            color="primary",
            outline=True
        ),
        dbc.Card(
            dbc.CardBody(
                [
                    html.H6("Average voting", className='card-title'), 
                    html.H4(id="average-vote", className='card-text')]
            ),
            color="primary",
            outline=True
        )
    ]
)

genre_graphs = html.Div([
    dbc.Row([
        dbc.Col(
            dbc.Card(
                [dbc.CardHeader(
                    html.H4(id="vote-plot-title")
                ),
                dbc.CardBody(
                    html.Iframe(
                        id="vote-plot",
                        style={
                            "border-width": "0",
                            "width": "100%",
                            "height": 265
                        },
                    )
                )], 
                color="success",
                outline=True
            )
        ),
        dbc.Col(
            dbc.Card(
                [dbc.CardHeader(
                    html.H4(id="revenue-plot-title")
                ),
                dbc.CardBody(
                    html.Iframe(
                        id="revenue-plot",
                        style={
                            "border-width": "0",
                            "width": "100%",
                            "height": 265
                        },
                    )
                )],
                color="success",
                outline=True
            )
        )
    ])
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
                    html.Iframe(
                        id="vote-scatter-plot",
                        style={
                            "border-width": "0",
                            "width": "100%",
                            "height": "400px"
                        },
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
    Output("vote-plot", "srcDoc"),
    Output("revenue-plot", "srcDoc"),
    Output("vote-scatter-plot", "srcDoc"),
    Output("average-revenue", "children"),
    Output("vote-plot-title", 'children'),
    Output("revenue-plot-title", 'children'),
    Output("vote-scatter-title", 'children'),
    Output("table-title", 'children'),
    Output("average-vote", "children"),
    Output("movies-data-frame", "children"),
    Input("xgenre-widget", "value"),
    Input("xbudget-widget", "value"),
)
def plot_altair(xgenre, budget):  # to add xbudget later
    studios_by_revenue = (
        movies.groupby("studios")["revenue"].median().sort_values().index.tolist()
    )
    filtered_movies = movies[movies["genres"] == xgenre].query(
        "@budget[0] < budget and budget < @budget[1]"
    )

    average_revenue = "US${:,.2f} mil".format(filtered_movies["revenue"].mean())

    average_vote = str(round(filtered_movies["vote_average"].mean(), 1))

    vote_chart = (
        alt.Chart(filtered_movies)
        .mark_boxplot(color="#20B2AA")
        .encode(
            alt.X("vote_average", title="Vote Average"),
            alt.Y("studios", sort=studios_by_revenue, title=None),
            tooltip="title",
        ).configure_axis(
            labelFontSize=12,
            titleFontSize=12
        ).properties(
            height=200,
            width=250
        ).interactive()
    )

    revenue_chart = (
        alt.Chart(filtered_movies)
        .mark_boxplot(color="#20B2AA")
        .encode(
            alt.X("revenue", title="Revenue (US$ mil)", axis=alt.Axis(format='$s')),
            alt.Y("studios", sort=studios_by_revenue, title=None),
            tooltip="title",
        ).configure_axis(
            labelFontSize=12,
            titleFontSize=12
        ).properties(
            height=200,
            width=250
        ).interactive()
    )

    vote_scatter_chart = (
        alt.Chart(filtered_movies)
        .mark_circle(color="#20B2AA")
        .encode(
            alt.X("vote_average", title="Vote Average"),
            alt.Y("vote_count", title="Vote Count"),
            tooltip="title",
        ).configure_axis(
            labelFontSize=12,
            titleFontSize=12
        ).properties(width=775)
    )  

    top_movies_df = (filtered_movies.nlargest(10, ["vote_average"]))[
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
        vote_chart.to_html(),
        revenue_chart.to_html(),
        vote_scatter_chart.to_html(),
        average_revenue,
        f'{xgenre} Movies Vote Average By Studio',
        f'{xgenre} Movies Financials By Studio',
        f'Voting Profile For {xgenre} Movies',
        f'Most Popular {xgenre} Movies (By Vote Average)',
        average_vote,
        dbc.Table.from_dataframe(
                top_movies_df,
                striped=True,
                bordered=True,
                hover=True
        )
    )


if __name__ == "__main__":
    app.run_server(debug=True)