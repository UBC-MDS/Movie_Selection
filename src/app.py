import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output
import altair as alt
import pandas as pd
import dash_bootstrap_components as dbc

# Read in global data
movies = pd.read_json("data/raw/lab2-movies.json")
boom_movies = movies.explode("studios").explode("genres")

# Setup app and layout/frontend
app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])
app.layout = dbc.Container(
    [
        html.H1("MOVIE SELECTION"),
        html.P(
            "A data visualization app that allows decision makers in the streaming companies to explore a dataset of movies to determine the popular movies that they need to provide to their users"
        ),
        dbc.Row(
            [
                dbc.Col(
                    [
                        dcc.Dropdown(
                            id="xgenre-widget",
                            value="Horror",  # REQUIRED to show the plot on the first page load
                            options=[
                                {"label": col, "value": col}
                                for col in boom_movies["genres"].unique()
                            ],
                        ),
                        html.Br(),
                        html.Br(),
                        dcc.RangeSlider(
                            id="xbudget-widget",
                            min=10_000_000,
                            max=300_000_000,
                            value=[10_000_000, 300_000_000],
                            marks={
                                10_000_000: "10",
                                100_000_000: "100",
                                200_000_000: "200",
                                300_000_000: "300M",
                            },
                        ),
                        html.Br(),
                        html.Br(),
                        dbc.Card(
                            dbc.CardBody(
                                [
                                    html.H6("Average box office value"),
                                    html.Div(id="average-revenue"),
                                ]
                            ),
                            color="light",
                        ),
                        html.Br(),
                        html.Br(),
                        dbc.Card(
                            dbc.CardBody(
                                [html.H6("Average voting"), html.Div(id="average-vote")]
                            ),
                            color="light",
                        ),
                    ],
                    md=2,
                ),
                dbc.Col(
                    [
                        dbc.Row(
                            [
                                dbc.Col(
                                    html.Iframe(
                                        id="vote-plot",
                                        style={
                                            "border-width": "0",
                                            "width": "150%",
                                            "height": "300px",
                                        },
                                    )
                                ),
                                dbc.Col(
                                    html.Iframe(
                                        id="revenue-plot",
                                        style={
                                            "border-width": "0",
                                            "width": "150%",
                                            "height": "300px",
                                        },
                                    )
                                ),
                            ]
                        ),
                        dbc.Row(
                            html.Iframe(
                                id="vote-scatter-plot",
                                style={
                                    "border-width": "0",
                                    "width": "100%",
                                    "height": "300px",
                                },
                            )
                        ),
                        dbc.Row(
                            html.Iframe(
                                id="movies-data-frame",
                                style={
                                    "border-width": "0",
                                    "width": "100%",
                                    "height": "300px",
                                },
                            )
                        ),
                    ]
                ),
            ]
        ),
    ]
)


# Set up callbacks/backend


@app.callback(
    Output("vote-plot", "srcDoc"),
    Output("revenue-plot", "srcDoc"),
    Output("vote-scatter-plot", "srcDoc"),
    Output("average-revenue", "children"),
    Output("average-vote", "children"),
    Input("xgenre-widget", "value"),
    Input("xbudget-widget", "value"),
)
def plot_altair(xgenre, budget):  # to add xbudget later
    studios_by_revenue = (
        boom_movies.groupby("studios")["revenue"].median().sort_values().index.tolist()
    )
    filtered_movies = boom_movies[boom_movies["genres"] == xgenre].query(
        "@budget[0] < budget and budget < @budget[1]"
    )

    average_revenue = "${:,}".format(round(filtered_movies["revenue"].mean()))
    average_vote = str(round(filtered_movies["vote_average"].mean(), 1))
    vote_chart = (
        alt.Chart(filtered_movies)
        .mark_boxplot(color="#20B2AA")
        .encode(
            alt.X("vote_average"),
            alt.Y("studios", sort=studios_by_revenue),
            tooltip="title",
        )
        .interactive()
    )

    revenue_chart = (
        alt.Chart(filtered_movies)
        .mark_boxplot(color="#20B2AA")
        .encode(
            alt.X("revenue"),
            alt.Y("studios", sort=studios_by_revenue),
            tooltip="title",
        )
        .interactive()
    )

    vote_scatter_chart = (
        alt.Chart(filtered_movies)
        .mark_circle(color="#20B2AA")
        .encode(alt.X("vote_average"), alt.Y("vote_count"), tooltip="title")
        .interactive()
    )
    return (
        vote_chart.to_html(),
        revenue_chart.to_html(),
        vote_scatter_chart.to_html(),
        average_revenue,
        average_vote,
    )


if __name__ == "__main__":
    app.run_server(debug=True)


# Notes
# 1. how to shorten call back
# 2. how to incorporate rangeslicer
# 3. formating card
# 4. overall aesthetic (esp left column)