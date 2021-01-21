#!/usr/bin/env python
# -*- coding: utf-8 -*-

# author: Vignesh Lashmi Rajakumar
# date: 2020-11-26

"""Import data and clean up for use in the dashboard
Usage: preprocess.py --datafile=<datafile> --out=<output-directory>

Options:
--datafile=<datafile>          path to data file
--out=<output_directory>       directory for saving processed file

Example:
    python src/preprocess.py --datafile=data/raw/lab2-movies.json --out=data/processed
"""
from docopt import docopt
import pandas as pd
import os

opt = docopt(__doc__)


def main(datafile, out):
    # load in the data
    movies = pd.read_json(datafile)

    # scale financials to millions
    movies.budget = movies.budget / 1000000
    movies.revenue = movies.revenue / 1000000

    # spot corrections in financials for two movies
    movies.loc[movies.id == 15417, "budget"] = (
        movies.loc[movies.id == 15417, "budget"] * 1000000
    )
    movies.loc[movies.id == 15417, "revenue"] = (
        movies.loc[movies.id == 15417, "revenue"] * 1000000
    )

    movies.loc[movies.id == 16340, "budget"] = (
        movies.loc[movies.id == 16340, "budget"] * 1000000
    )
    movies.loc[movies.id == 16340, "revenue"] = (
        movies.loc[movies.id == 16340, "revenue"] * 1000000
    )

    # explode
    movies = movies.explode("studios").explode("genres")

    # calculate new financial columns
    movies["profit"] = movies.revenue - movies.budget
    movies["profit_margin"] = movies.profit / movies.revenue

    # save new file
    if not os.path.exists(out):
        os.makedirs(out)

    movies.to_csv(f"{out}/movies.csv", index=False)


if __name__ == "__main__":
    main(opt["--datafile"], opt["--out"])
