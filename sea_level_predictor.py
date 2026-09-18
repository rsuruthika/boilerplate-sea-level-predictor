import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress


def draw_plot():
    df = pd.read_csv("epa-sea-level.csv")

    fig, ax = plt.subplots()

    # Scatter plot
    ax.scatter(
        df["Year"],
        df["CSIRO Adjusted Sea Level"]
    )

    # Line of best fit for all data
    slope, intercept, r_value, p_value, std_err = linregress(
        df["Year"],
        df["CSIRO Adjusted Sea Level"]
    )

    years = pd.Series(range(1880, 2051))
    sea_levels = slope * years + intercept

    ax.plot(years, sea_levels)

    # Line of best fit for data from 2000
    recent_df = df[df["Year"] >= 2000]

    slope2, intercept2, r_value2, p_value2, std_err2 = linregress(
        recent_df["Year"],
        recent_df["CSIRO Adjusted Sea Level"]
    )

    recent_years = pd.Series(range(2000, 2051))
    recent_sea_levels = slope2 * recent_years + intercept2

    ax.plot(recent_years, recent_sea_levels)

    # Labels and title
    ax.set_xlabel("Year")
    ax.set_ylabel("Sea Level (inches)")
    ax.set_title("Rise in Sea Level")

    # Save plot
    fig.savefig("sea_level_plot.png")

    # Return Axes, not Figure
    return ax