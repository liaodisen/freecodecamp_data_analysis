import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    filepath = 'epa-sea-level.csv'
    df = pd.read_csv(filepath)

    # Create scatter plot
    fig, ax = plt.subplots()
    fig.set_figheight(6)
    fig.set_figwidth(14)
    ax.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])

    # Create first line of best fit
    data = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    years = np.arange(1880, 2051)
    ax.plot(years, data.slope*years+data.intercept)
    # Create second line of best fit
    df2 = df[df['Year']>2000]
    data2 = linregress(df2['Year'], df2['CSIRO Adjusted Sea Level'])
    years2 = np.arange(2000, 2051)
    ax.plot(years2, data2.slope*years2+data2.intercept)

    # Add labels and title
    ax.set_xlabel("Year")
    ax.set_ylabel("Sea Level (inches)")
    ax.set_title("Rise in Sea Level")
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()